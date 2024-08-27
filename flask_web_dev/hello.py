"""
Flask Practice
"""
from flask import Flask
from dotenv import load_dotenv

# Load environment vars
load_dotenv()

app = Flask(__name__)  # __name__ grabs current file - denotes we are not running an imported module
print(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func()}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return f'<em>{func()}</em>'
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f'<u>{func()}</u>'
    return wrapper

@app.route("/")
def hello_world():
    return ('<div style="text-align:center">'
            '<h1>Hello, World!</h1>'
            '<p>Hey everyone - Cringe</p>'
            '<iframe src="https://giphy.com/embed/tMESZEb7xNFbaLnPjw" width="369" height="480" style="" '
            'frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/moodman-'
            'elon-musk-breakthrough-prize-tMESZEb7xNFbaLnPjw"></a></p>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWh3OHo4MDJzcTV4NmE0aXdtb2IyOW54NnptZHY2dWkxeGRr'
            'NGYwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/b4K0MfAZNLiQDqgYJN/giphy.gif">'
            '<img src="https://media.giphy.com/media/czlgsWC0PPqVzxuQzN/giphy.gif?cid=ecf05e474ajpv4nb1smnikz2mvqf72vcz'
            'bzw6oiyqiecbi7y&ep=v1_gifs_related&rid=giphy.gif&ct=g">'
            '<img style="width: 100vw;height: 100vh" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2s3dzFhOTIyaG'
            'htbTd2bnhpZj'
            'Q0c3U2Y3d0MHN5Mmxscm9jNG'
            'NwZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fr5LA2RCQbnVp74CxH/giphy.gif">'
            '</div>'
            )

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye</p>"

# Get url vars dynamically <var> = makes var with that name
# Can use a convert int: to change data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello {name}! You are number {number}</p>"


# Start without using terminal - debug on to enable reloading and logs
if __name__ == "__main__":
    app.run(debug=True)
