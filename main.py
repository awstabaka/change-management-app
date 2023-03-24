from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Kamil',
        'title': 'First test post',
        'content': 'First test post content',
        'date_posted': '23/03/2023'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home", posts=posts)


@app.route('/history')
def history():
    return render_template("history.html", title="About")
