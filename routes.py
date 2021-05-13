from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.forms import UserPhoneNumber, UserInfoForm, LoginForm
from app.models import User

@app.route('/')
def index():
    context = {
        'title': 'Home',
        'posts': Post.query.all(),
        'user': {
            'id': 2,
            'username': 'Felix'
        }
    }
    return render_template('index.html', **context)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'REGISTER PHONE NUMBER'
    form = UserPhoneNumber()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phonenumber = form.phone_number.data
        existing_phonenumber = User.query.filter((User.username == username) | (User.email == email) | (User.phone == phonenumber)).all()
        if existing_phonenumber: 
            flash('Well, looks like you already have a log with us!', 'danger')
            return redirect(url_for('register'))
        
        new_phonenumber = User(username,email,phonenumber)
        db.session.add(new_phonenumber)
        db.session.commit()
        
        flash(f'Thank you {username} for your registration!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', title=title, form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login Here!'
    form = LoginForm()
    if request.method == 'POST': and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Sorry, No Correct Username Detected')
    return render_template('login.html', title=title, form=form)