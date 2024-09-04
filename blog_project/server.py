from flask import Flask, render_template
from dotenv import load_dotenv
from datetime import datetime
import requests
from random import randint

load_dotenv()

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


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


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
