from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, exc
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.secret_key = os.environ.get("SECRET_KEY")


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    return user

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # noinspection PyArgumentList
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(password=request.form.get("password"), method='scrypt', salt_length=8)
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError:
            flash("This email is already registered! Please login instead.")
            return redirect(url_for("login"))
        else:
            # log in user after registering
            login_user(new_user)
            flash(f"Successfully registered! Welcome {new_user.name}!")
            return redirect(url_for("secrets"))

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    user = db.session.execute(db.select(User).where(User.email == request.form.get("email"))).scalar()

    if request.method == "POST" and user is not None:
        if check_password_hash(user.password, request.form.get("password")):
            login_user(user)

            flash("Logged in Successfully!")
            print(user)
            return redirect(url_for("home"))
        else:
            # if invalid
            flash("Invalid credentials try again!")
            return redirect(url_for("login"))
    elif request.method == "POST" and user is None:
        # If wrong email redirect back to log in form
        flash("Sorry, that email doesn't exist in our database!")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/secrets', methods=["GET"])
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
@login_required
def logout():
    # logs out active user
    logout_user()
    return redirect(url_for("home"))

@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory("./static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
