from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
import smtplib
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect

load_dotenv()

PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL = os.environ.get("EMAIL")
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
HOST = "smtp.gmail.com"

# Create WTF form class
class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    # render_kw sets a keyword for the button, can be used to ID which button is primary if many are on a page
    submit = SubmitField(label="Log In", render_kw={'btn-primary': 'True'})


app = Flask(__name__)

# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
csrf = CSRFProtect(app)

# init Bootstrap5 for Flask
bootstrap = Bootstrap5(app)

@app.route("/")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_blog_posts = response.json()
    return render_template(template_name_or_list="index.html", posts=all_blog_posts)


@app.route(rule="/posts/<num>")
def get_blog_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_blog_posts = response.json()
    return render_template(template_name_or_list="post.html", posts=all_blog_posts, num=num)


@app.route(rule="/about")
def get_about():
    return render_template("about.html")


@app.route(rule="/login", methods=["GET", "POST"])
def login_form():
    form = MyForm()
    print(form.email.data)
    print(form.password.data)
    # Add validation to form - if  form is validated then show denied or granted
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template(template_name_or_list="success.html")
        else:
            return render_template(template_name_or_list="denied.html")
    return render_template(template_name_or_list="login.html", form=form)

# # Add routes for success/denied
# @app.route("/login/success")
# def success_login():
#     return render_template(template_name_or_list="success.html")

@app.route(rule="/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html")

    if request.method == "POST":
        connection = smtplib.SMTP(host=HOST)
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Blog Message\n\n "
                f"Name: {request.form['name']}\n "
                f"Email: {request.form['email']}\n "
                f"Phone: {request.form['telephone']}\n "
                f"Message: {request.form['message']}"
        )
        return render_template("contact.html")


# Note the [] array for method - can have more than one HTTP method on a route
# @app.route("/form-entry", methods=["POST"])
# def get_user_form():
#

# Create new route to take in a users name and guess their gender/age with api calls
# genderize.io and agify.io apis
@app.route(rule="/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    return render_template(template_name_or_list="guess.html", age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
