from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
from random import randint
import os

load_dotenv()

app = Flask(__name__)

# Create the Base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Data Model - Mapped used to typecheck the data
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection-db.db"
# init app with extension
db.init_app(app)

# Use app context to interact with DB if no front end
with app.app_context():
    db.create_all()

# ========= CRUD operations ==========
# Add book to DB
with app.app_context():
    book = Books(
        id=randint(0, 1000),  # The primary-key field will be auto generated if not included here
        title="The AAAAATree",
        author="Some Dude",
        rating=9.8
    )
    # db.session is used to query and interact with the DB
    db.session.add(book)
    db.session.commit()

# Read from DB - scalars gets individual entries
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    print(all_books)

# Read a specific record - scalar for just one entry
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Holes")).scalar()
    print(book)  # Returns the id of the book

# Update record by Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Moby Dick")).scalar()
    book_to_update.title = "Moby"
    db.session.commit()

# Update record with Primary Key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     or book_to_update = db.get_or_404(Books, book_id)
    book_to_update.title = "To Kill a Mockingbird"
    db.session.commit()

# Delete record with Primary Key - get_or_404 will raise a 404 if not found otherwise it will return the instance
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id))
    #     or book_to_update = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()


# if __name__ == "__main__":
#     app.run(debug=True)

