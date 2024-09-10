from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


load_dotenv()
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")

app = Flask(__name__)

# Create the Base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection-db.db"
# init app with extension
db.init_app(app)

# Data Model - Mapped used to typecheck the data
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# Only need if instance does not already exist
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection-db.db"
# init app with extension
# db.init_app(app)

# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
csrf = CSRFProtect(app)

# Flask Bootstrap
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    # Read DB
    with app.app_context():
        results = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = results.scalars().all()
        print(all_books)

    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    class BookForm(FlaskForm):
        book_name = StringField(label="Book Name", validators=[DataRequired()])
        book_author = StringField(label="Book Author", validators=[DataRequired()])
        rating = StringField(label="Rating", validators=[DataRequired()])
        add_button = SubmitField(label="Submit")

    form = BookForm()

    if form.validate_on_submit():
        new_book = Books(
            title=form.book_name.data,
            author=form.book_author.data,
            rating=form.rating.data,
        )

        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for("home"))

    return render_template("form.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit_book():
    # use request.args to get parameters sent to the url (query)
    book_id = request.args.get('id')
    print(book_id)

    class EditForm(FlaskForm):
        rating = StringField(label="Rating", validators=[DataRequired()])
        add_button = SubmitField(label="Submit")


    edit_form = EditForm()

    if edit_form.validate_on_submit():
        # update in db
        with app.app_context():
            book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
            book_to_update.rating = edit_form.rating.data
            db.session.commit()

        return redirect(url_for("home"))

    return render_template("form.html", form=edit_form)

@app.route("/delete", methods=["GET", "POST"])
def delete_book():
    # use request.args to get parameters sent to the url (query)
    book_id = request.args.get('id')
    print(book_id)

    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    #     or book_to_update = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

