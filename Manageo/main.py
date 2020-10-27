from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .form import requestForm
from .models import Log
from . import db
import uuid
import os
from werkzeug.utils import secure_filename




main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')



@main.route('/profile')
@login_required
def profile():

    demand = Log.query.filter_by(user_id = current_user.id)
    demands = demand.all()

    first_name = current_user.user_first_name
    last_name = current_user.user_last_name
    admin = current_user.is_admin

    return render_template('account.html', admin = admin, first_name = first_name, last_name = last_name, demands = demands )

@main.route('/profile/demandes')
@login_required
def requests():
    form = requestForm()

    return render_template("requests.html", form = form)

@main.route('/profile/demandes', methods=["POST"])
@login_required
def requests_post():
    form = requestForm()
    UPLOAD_FOLDER = '/download'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    if form.validate_on_submit:
        siret = form.siret.data
        societyName = form.societyName.data
        request = form.request.data
        file = form.file.data

        """if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))"""
            
        

        print(siret, societyName, request)

        log = Log(log_id = uuid.uuid4(), log_category = request, log_siret = siret, log_society_name = societyName.lower(), user_id = current_user.id)
        db.session.add(log)
        db.session.commit()

    return render_template("requests.html", form = form)