from flask import render_template, url_for, flash, redirect
from main import app
from main.forms import RegistrationForm, LoginForm
from main.modules import User, Post


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
