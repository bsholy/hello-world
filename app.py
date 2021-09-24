from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/test_page')
def test_page():
    return render_template('TestPage.html')