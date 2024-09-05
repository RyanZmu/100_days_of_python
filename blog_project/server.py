from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import smtplib
import requests

load_dotenv()

PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL = os.environ.get("EMAIL")
HOST = "smtp.gmail.com"

app = Flask(__name__)

@app.route("/")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_blog_posts = response.json()
    return render_template("index.html", posts=all_blog_posts)


@app.route("/posts/<num>")
def get_blog_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_blog_posts = response.json()
    return render_template("post.html", posts=all_blog_posts, num=num)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
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
@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    return render_template("guess.html", age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
