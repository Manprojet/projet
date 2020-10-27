from flask import Blueprint, render_template, redirect, request, flash, url_for, Flask
from Manageo.form import registerForm, loginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user, current_user, login_required
from .models import User, MyModelView
from . import db, admin



auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = loginForm()
    return render_template('login.html', form = form)


@auth.route('/login', methods = ['POST'])
def login_post():
    form = loginForm()
    email = form.email.data
    mdp = form.password.data
    remember = True if form.remember.data else False


    user = User.query.filter_by(user_email = email).first()


    if not user or not check_password_hash(user.mdp_hash, mdp):
        flash('Identifiant incorrect, veuillez réessayer')
        return redirect(url_for('auth.login'))

    login_user(user, remember = remember)

    if current_user.is_admin:
        return redirect('/admin')

    return redirect(url_for('main.profile'))

    
@auth.route('/signup')
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = registerForm()

    return render_template('signup.html', form = form)

@auth.route('/signup', methods = ['POST'])
def signup_post():

    form = registerForm()

    if form.validate_on_submit():

        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        mdp = form.password.data
        mdp_hash = generate_password_hash(mdp, method='sha256')


        new_user = User(user_email = email, user_first_name = first_name, user_last_name = last_name, user_adress = address, user_phone = phone, mdp_hash = mdp_hash)
        db.session.add(new_user)
        db.session.commit()

        new_user._mailRegister()
    
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

