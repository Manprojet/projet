from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    first_name = current_user.user_first_name
    last_name = current_user.user_last_name

    return render_template('account.html', first_name = first_name, last_name = last_name)

