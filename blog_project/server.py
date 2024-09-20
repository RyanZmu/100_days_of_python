from crypt import methods
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_ckeditor import CKEditorField, CKEditor
from flask_ckeditor.utils import cleanify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os
import smtplib
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, URLField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect

load_dotenv()

PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL = os.environ.get("EMAIL")
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
HOST = "smtp.gmail.com"


app = Flask(__name__)
ckeditor = CKEditor(app)

# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Enable CSRF
csrf = CSRFProtect(app)

# DB
# Create the Base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class NewPost(FlaskForm):
    title = StringField(label="Blog Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    body = CKEditorField(label="Blog Body", validators=[DataRequired()])
    img_url = URLField(label="Image URL", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    date: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    img_url: Mapped[str] = mapped_column(String(255), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(255), nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
# init app with extension
db.init_app(app)

# init Bootstrap5 for Flask
bootstrap = Bootstrap5(app)

@app.route("/")
def get_blog():
    all_blog_posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template(template_name_or_list="index.html", posts=all_blog_posts)


@app.route(rule="/posts/<post_id>")
def get_blog_post(post_id):
    post_to_display = db.get_or_404(BlogPost, post_id)
    return render_template(template_name_or_list="post.html", post=post_to_display)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = NewPost()

    if form.validate_on_submit():
        post = BlogPost(
            title=form.data.get("title"),
            date=datetime.now().strftime("%B %w, %Y"),
            body=form.data.get("body"),
            author=form.data.get("author"),
            img_url=form.data.get("img_url"),
            subtitle=form.data.get("subtitle")
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_blog"))

    return render_template("new_post.html", form=form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)

    edit_form = NewPost(
        title=post_to_edit.title,
        date=post_to_edit.date,
        body=post_to_edit.body,
        author=post_to_edit.author,
        img_url=post_to_edit.img_url,
        subtitle=post_to_edit.subtitle,
    )

    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.data.get("title")
        post_to_edit.body = edit_form.data.get("body")
        post_to_edit.author = edit_form.data.get("author")
        post_to_edit.img_url = edit_form.data.get("img_url")
        post_to_edit.subtitle = edit_form.data.get("subtitle")

        db.session.commit()
        return redirect(url_for("get_blog_post", post_id=post_to_edit.id))

    return render_template("new_post.html", form=edit_form)


@app.route("/delete/<post_id>", methods=["GET"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)

    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_blog"))


@app.route(rule="/about")
def get_about():
    return render_template("about.html")


@app.route(rule="/login", methods=["GET", "POST"])
def login_form():
    # Create WTF form class
    class MyForm(FlaskForm):
        email = StringField(label='Email', validators=[DataRequired(), Email()])
        password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
        # render_kw sets a keyword for the button, can be used to ID which button is primary if many are on a page
        submit = SubmitField(label="Log In", render_kw={'btn-primary': 'True'})

    form = MyForm()

    # Add validation to form - if  form is validated then show denied or granted
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template(template_name_or_list="success.html")
        else:
            return render_template(template_name_or_list="denied.html")
    return render_template(template_name_or_list="login.html", form=form)


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


if __name__ == '__main__':
    app.run(debug=True)
