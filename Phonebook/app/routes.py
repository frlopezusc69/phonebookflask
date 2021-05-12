from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserInfoForm
from app.models import User, Post

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
    form = UserInfoForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phonenumber = form.phonenumber.data
        existing_phonenumber = User.query.filter(User.username == username) | (User.email == email) | (User.phonenumber == phonenumber).all()
        if existing_phonenumber: 
            flash('Well, looks like you already have a log with us!', 'danger')
            return redirect(url_for('register.php'))
        
    new_phonenumber = User(username,email,phonenumber)
    db.session.add(new_phonenumber)
    db.session.commit()
    
    flash(f'Thank you {username} for your registration!', 'success')
    return redirect(url_for('index'))

    return render_template('register.html', title=title, form = form)