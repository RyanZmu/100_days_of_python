from crypt import methods

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField, TimeField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import random as r
import pandas

# Load vars
load_dotenv()
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
TOP_SECRET = os.environ.get("TOP_SECRET")

app = Flask(__name__)

# DB
# Create the Base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
# init app with extension
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    has_sockets: Mapped[int] = mapped_column(Integer, nullable=False)
    has_toilet: Mapped[int] = mapped_column(Integer, nullable=False)
    has_wifi: Mapped[int] = mapped_column(Integer, nullable=False)
    can_take_calls: Mapped[int] = mapped_column(Integer, nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee_price: Mapped[float] = mapped_column(Float, nullable=False)

    def to_dict(self):
        # Gets column.name and finds all attrs for it and uses that for the value and creates a dict
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
# csrf = CSRFProtect(app)

# init Bootstrap5 for Flask
bootstrap = Bootstrap5(app)

# Create form to add Cafe
class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    location = URLField(label="Location", validators=[DataRequired()])
    opening = TimeField(label="Opening Time", validators=[DataRequired()])
    closing = TimeField(label="Closing Time", validators=[DataRequired()])
    coffee = SelectField(label="Coffee Quality", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField(label="Wifi Quality", choices=["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField(label="Power Quality", choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label="Submit!", validators=[DataRequired()])

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    data = pandas.read_csv("./data/cafe-data.csv")
    # orient records to get column+row to line up {"Cafe Name": "Lighthaus"}
    data_dict = data.to_dict(orient="records")

    print(data_dict)
    return render_template("cafe.html", cafe_data=data_dict)


@app.route("/cafes/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        user_data = {
            "Cafe Name": form.cafe_name.data,
            "Location": form.location.data,
            "Open": form.opening.data,
            "Close": form.closing.data,
            "Coffee": form.coffee.data,
            "Wifi": form.wifi.data,
            "Power": form.power.data
        }

        # Read data and append new data
        data = pandas.read_csv("./data/cafe-data.csv", index_col=False)
        new_data = data._append(user_data, ignore_index=True)

        # Write new data to csv
        print(new_data)
        new_data.to_csv("./data/cafe-data.csv", index=False)

    return render_template("add.html", form=form)


# API Routes
@app.route("/api/random", methods=["GET"])
def random_call():
    cafes_list = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = r.choice(cafes_list)
    print(random_cafe.name)
    # Return JSON data of a random cafe - Two Methods
    # Method 1:
    # return jsonify(
    #     id=random_cafe.id,
    #     name=random_cafe.name,
    #     map_url=random_cafe.map_url,
    #     img_url=random_cafe.img_url,
    #     location=random_cafe.location,
    #     has_sockets=random_cafe.has_sockets,
    #     has_toilet=random_cafe.has_toilet,
    #     has_wifi=random_cafe.has_wifi,
    #     can_take_calls=random_cafe.can_take_calls,
    #     seats=random_cafe.seats,
    #     coffee_price=random_cafe.coffee_price)

    # Method 2:
    # Takes the dict made with to_dict() and uses those for the json object instead of typing it all out like above
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/api/all", methods=["GET"])
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

    # Loop over each cafe and use to_dict() method
    cafes_list = [cafe.to_dict() for cafe in all_cafes]
    print(cafes_list)

    return jsonify(cafes=cafes_list)


@app.route("/api/search")
def cafe_search():
    location_requested = request.args.get("loc")

    db_result = db.session.execute(db.select(Cafe).where(Cafe.location == location_requested)).scalar()

    # Check if cafe result is found, if not then return an error
    if db_result is not None:
        return jsonify(db_result.to_dict())
    else:
        return jsonify(
            error={
               "Not Found": "Sorry this location has no cafe data!"
            }
        )


@app.route("/api/add", methods=["POST", "GET"])
def add_cafe_api():
    # POST request sends a form data type we can use x-www-form-urlencoded
    print(request.form.get("name"))

    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=request.form.get('has_sockets'),
        has_toilet=request.form.get('has_toilet'),
        has_wifi=request.form.get('has_wifi'),
        can_take_calls=request.form.get('can_take_calls'),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={
        "success": "Successfully added the new cafe."
    })


@app.route("/api/update/<cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    requested_cafe = db.session.get(Cafe, cafe_id)
    new_price = request.args.get('new_price')

    if requested_cafe is not None:
        # Update price with query param
        requested_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully Updated the coffee price."}), 200
    else:
        return jsonify(error={"Not Found": "That Cafe ID is invalid please try another!"}), 404


@app.route("/api/delete/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    requested_db = db.session.get(Cafe, cafe_id)
    sent_key = request.args.get("apikey")

    if requested_db and sent_key == TOP_SECRET:
        db.session.delete(requested_db)
        db.session.commit()
        return jsonify(response={"Success": "Cafe has been successfully deleted."}), 200
    elif sent_key != TOP_SECRET:
        return jsonify(error={"Bad Key": "Sorry not allowed, please provide a correct API KEY"}), 403
    elif requested_db is None:
        return jsonify(error={"Not Found": "Sorry this cafe ID does not exist"}), 404


if __name__ == "__main__":
    app.run(debug=True)
