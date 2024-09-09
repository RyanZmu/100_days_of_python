from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect
import os
import pandas

# Load vars
load_dotenv()
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")

app = Flask(__name__)

# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
csrf = CSRFProtect(app)

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


if __name__ == "__main__":
    app.run(debug=True)
