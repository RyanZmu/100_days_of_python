"""
Personal Website
- Create a simple website using HTML templates
- Have an index for '/' route and another template for /<name>
- Load HTML template
"""
from dotenv import load_dotenv
from flask import Flask, render_template, url_for

# Load vars
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def user_screen(name):
    return render_template(f'{name}.html')


if __name__ == '__main__':
    app.run(debug=True)
