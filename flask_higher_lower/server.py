"""
Flash Higher-Lower Game

- Create home domain to display "Guess a number between 0 - 9"
- Generate a random number between 0-9
- User goes to domain/<number> and will see a gif and message saying if they're too high, too low or correct

"""
from random import randint
from flask import Flask
from dotenv import load_dotenv

# Load environment vars
load_dotenv()

app = Flask(__name__)

number = randint(0, 9)

@app.route("/")
def greeting():
    return f"Guess a number between 0 and 9"

# Use get number_guessed from the url and pass into the check_winner func
@app.route("/<number_guessed>")
def check_winner(number_guessed):
    if int(number_guessed) == number:
        return (f"<p>Wow Good Guess! The answer is {number_guessed}</p>"
                f"<img src=''>")
    elif int(number_guessed) < number:
        return "<p>Too Low!</p>"
    elif int(number_guessed) > number:
        return "<p>Too High!</p>"


if __name__ == "__main__":
    app.run(debug=True)
