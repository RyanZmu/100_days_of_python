from __future__ import annotations
from typing import List

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float, exc, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from dotenv import load_dotenv
import os
import smtplib
from forms import NewPost, LoginForm, RegisterForm, CommentForm
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

load_dotenv()

PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL = os.environ.get("EMAIL")
SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
HOST = "smtp.gmail.com"

app = Flask(__name__)

ckeditor = CKEditor(app)

# Enable CSRF
csrf = CSRFProtect(app)
# Config app for CSFR with a secret key
app.config["SECRET_KEY"] = SECRET_KEY
# Add app's secret key
app.secret_key = os.environ.get("APP_SECRET_KEY")

# DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # This will act like a List of BlogPost objects attached to each User.
    # Every User class will have a posts list
    posts = relationship("BlogPosts", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class BlogPosts(db.Model):
    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, user.id that refers to User table - ties the value of author_id to the User.id
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey(column="users.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    date: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(String(255), nullable=False)
    img_url: Mapped[str] = mapped_column(String(255), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(255), nullable=False)
    # Create ref to the User object. the posts refers to the posts property of User class
    author = relationship("User", back_populates="posts")
    # Holds all comments for this post
    post_comments = relationship("Comment", back_populates="parent_post")

class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey(column="users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_posts.id"))
    comment_body: Mapped[str] = mapped_column(String(255), nullable=False)
    author = relationship("User", back_populates="comments")
    parent_post = relationship("BlogPosts", back_populates="post_comments")



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
# init app with extension
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

# init Bootstrap5 for Flask
bootstrap = Bootstrap5(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/")
def get_blog():
    all_blog_posts = db.session.execute(db.select(BlogPosts)).scalars().all()
    return render_template(template_name_or_list="index.html", posts=all_blog_posts)


@app.route(rule="/posts/<post_id>", methods=["GET", "POST"])
def get_blog_post(post_id):
    # Get post
    post_to_display = db.get_or_404(BlogPosts, post_id)

    # Add Comments to post
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        if current_user.is_active:
            new_comment = Comment(
                author_id=current_user.id,
                post_id=post_id,
                comment_body=comment_form.data.get("comment")
            )

            db.session.add(new_comment)
            db.session.commit()
            flash("Comment added!")
            return redirect(url_for("get_blog_post", post_id=post_id))
        else:
            flash("Please Login to comment!")
            return redirect(url_for("login_form"))

    return render_template(
        template_name_or_list="post.html",
        post=post_to_display,
        comment_form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@login_required
def new_post():
    form = NewPost()

    if form.validate_on_submit():
        post = BlogPosts(
            author_id=current_user.id,
            title=form.data.get("title"),
            date=datetime.now().strftime("%B %w, %Y"),
            body=form.data.get("body"),
            img_url=form.data.get("img_url"),
            subtitle=form.data.get("subtitle")
        )

        try:
            db.session.add(post)
            db.session.commit()
        except exc.IntegrityError:
            # Add flash
            flash("Post with this title Exists")
            return redirect(url_for("get_blog"))
        else:
            return redirect(url_for("get_blog"))

    return render_template("forms.html", form=form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPosts, post_id)

    edit_form = NewPost(
        title=post_to_edit.title,
        date=post_to_edit.date,
        body=post_to_edit.body,
        img_url=post_to_edit.img_url,
        subtitle=post_to_edit.subtitle,
    )

    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.data.get("title")
        post_to_edit.body = edit_form.data.get("body")
        post_to_edit.img_url = edit_form.data.get("img_url")
        post_to_edit.subtitle = edit_form.data.get("subtitle")

        db.session.commit()
        return redirect(url_for("get_blog_post", post_id=post_to_edit.id))

    return render_template("forms.html", form=edit_form, post_id=post_to_edit.id)


# def admin_only():
#     def inner(current_user):
#         if current_user.id != 1:
#             abort(403)
#     return inner


@app.route("/delete/<post_id>", methods=["GET"])
@login_required
def delete_post(post_id):
    # Delete the blogpost AND comments associated with blogpost
    db.session.execute(db.delete(Comment).where(Comment.post_id == post_id))
    db.session.execute(db.delete(BlogPosts).where(BlogPosts.id == post_id))
    db.session.commit()
    return redirect(url_for("get_blog"))


@app.route(rule="/about")
def get_about():
    return render_template("about.html")


@app.route(rule="/login", methods=["GET", "POST"])
def login_form():
    form = LoginForm()

    user_email = form.data.get("email")
    user_password = form.data.get("password")

    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()

        if user is not None:
            if check_password_hash(user.password, user_password):
                login_user(user)
                return redirect(url_for("get_blog"))
        else:
            flash("Invalid email or Password!")

    return render_template(template_name_or_list="forms.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("get_blog"))


@app.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegisterForm()

    if form.validate_on_submit():
        # noinspection PyArgumentList
        new_user = User(
            email=form.data.get("email"),
            password=generate_password_hash(form.data.get("password"), method="scrypt", salt_length=10),
            username=form.data.get("username")
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError:
            # Add flash
            flash("User exists with this email!")
        else:
            login_user(new_user)
            return redirect(url_for("get_blog"))

    return render_template(template_name_or_list="forms.html", form=form)


@app.route(rule="/contact", methods=["POST", "GET"])
# @admin_only
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
