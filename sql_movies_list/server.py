from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, URLField, FloatField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

load_dotenv()
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
TMDB_KEY = os.environ.get("TMDB_KEY")
TMDB_ACCESS_TOKEN = os.environ.get("TMDB_ACCESS_TOKEN")
TMDB_MOVIE_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)

# Create the Base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# Only need if instance does not already exist
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-db.db"
# init app with extension
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[int] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# Create an initial DB entry
new_movie = Movie(
    title="Cars",
    year="2006",
    description="On the way to the biggest race of his life, a hotshot rookie race car gets stranded in a rundown "
                "town and learns that winning isn't everything in life.",
    rating=8.3,
    ranking=3,
    review="Cars go VROOOM",
    img_url="https://image.tmdb.org/t/p/original/eN0OtsqjwA88c9lECa9RldJeW3w.jpg"
)

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
csrf = CSRFProtect(app)

# Flask Bootstrap
bootstrap = Bootstrap5(app)

# Routes
@app.route("/")
def home():
    # Get movies from DB
    with app.app_context():
        movies_sort_by_rank = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    highest_rank = 11  # will start at 10
    highest_rating = 0.0

    for movie in movies_sort_by_rank:
        # print(movie)
        if movie.rating > highest_rating:
            highest_rating = movie.rating
            highest_rank -= 1

            with app.app_context():
                movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie.id)).scalar()
                movie_to_update.ranking = highest_rank
                db.session.commit()

    return render_template("index.html", movies=movies_sort_by_rank)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    class AddForm(FlaskForm):
        title = StringField(label="Title", validators=[DataRequired()])
        submit = SubmitField(label="Submit")

    form = AddForm()
    movie_searched = form.title.data
    # Use movie db API to allow a user to search a movie title and select the correct one to add
    params = {
        "api_key": TMDB_KEY,
        "query": movie_searched
    }

    movie_request = requests.get(TMDB_MOVIE_SEARCH_ENDPOINT, params=params)
    movie_search_return = movie_request.json()

    # print(movie_search_return)
    movie_list = movie_search_return["results"]
    # print(movie_list)

    if form.validate_on_submit():
        return render_template("select.html", movie_list=movie_list)

    movie_id = request.args.get("id")
    if movie_id is not None:
        print(movie_list)
        get_params = {
            "api_key": TMDB_KEY,
        }

        # Get requested movie info from api
        get_movie_by_id = f"https://api.themoviedb.org/3/movie/{movie_id}"
        get_movie_request = requests.get(get_movie_by_id, params=get_params)
        movie_return = get_movie_request.json()
        print(movie_return)

        # Create new DB entry for movie - default rating ranking initially
        movie_to_add = Movie(
            title=movie_return["title"],
            year=movie_return["release_date"][:4],
            description=movie_return["overview"],
            rating=0.0,
            ranking=0,
            review="None",
            img_url=f"https://image.tmdb.org/t/p/original{movie_return['poster_path']}"
        )

        # Add the movie and redirect to edit the rating/ranking and review
        with app.app_context():
            db.session.add(movie_to_add)
            # Search for ID in DB of the movie just added
            movies = db.session.execute(db.select(Movie)).scalars().all()
            for movie in movies:
                if movie.title == movie_to_add.title:
                    movie_id = movie.id
                    print({"movie add": movie_id})

                    # commit changes and redirect to edit after movie is added to DB to set
                    db.session.commit()
                    return redirect(url_for("edit_movie", id=movie_id))

    print(movie_id)

    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    class EditForm(FlaskForm):
        rating = FloatField(label="Rating 0/10")
        review = StringField(label="Review")
        submit = SubmitField(label="Submit")

    form = EditForm()
    movie_id = request.args.get("id")

    if form.validate_on_submit():
        with app.app_context():
            movie_to_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

            movie_to_edit.rating = form.rating.data
            movie_to_edit.review = form.review.data

            db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get("id")

    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)