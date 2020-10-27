from . import db, mail
from flask import abort
from flask_login import UserMixin, current_user
from flask_mail import Message, Mail
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

class User(UserMixin, db.Model):  #classe utilisateur et bdd
    __tablename__ = 'users'
    
    id = db.Column('user_id', db.Integer, primary_key = True)  
    user_first_name = db.Column('user_first_name', db.String(50))
    user_last_name = db.Column('user_last_name', db.String(50))
    mdp_hash = db.Column('mdp_hash', db.String(70))
    user_email = db.Column('user_email', db.String(320), unique = True)
    user_adress = db.Column('user_adress', db.String())
    user_phone = db.Column('user_phone', db.String(20))
    is_admin = db.Column(db.Boolean, default=False)
    society = db.relationship('Society', backref = "user")
    admin_id = db.relationship('Log', backref = "admin", foreign_keys = 'Log.log_admin_id')
    user = db.relationship('Log', backref = "user", foreign_keys = 'Log.user_id')

    def _mailRegister(self): #envoi mail inscription 
       
        msg = Message('Inscription Manageo-RGPD', 
                    recipients = [self.user_email])
        msg.body = "Bonjour {prenom} {nom}, votre inscription à bien été prise en compte. Votre espace personnel est accessible dès maintenant.".format(nom= self.user_last_name, prenom = self.user_first_name)
        msg.html = 'Bonjour {nom} {prenom}, votre inscription à bien été prise en compte.<br> Votre espace personnel est accessible dès maintenant. <br> <a href = "localhost:5000/login">Connection</a>'.format(nom= self.user_last_name, prenom = self.user_first_name)
        mail.send(msg)



class MyModelView(ModelView):

    def is_accessible(self):

        if current_user.is_authenticated and current_user.is_admin:
           return current_user.is_authenticated
       
        return abort(404)


class Society(db.Model):
    __tablename__ = 'society_infos'
    
    id = db.Column('soc_id', db.Integer, primary_key = True)
    soc_reason = db.Column('soc_reason', db.String(400))
    soc_siret = db.Column('soc_siret', db.BigInteger())
    soc_type = db.Column('soc_type', db.Enum("SAS", "SARL", "SASU", "SCI", "AI", "SA"))
    soc_employee_num = db.Column('soc_employee_num', db.Integer)
    soc_address = db.Column('soc_address', db.String(400))
    soc_status = db.Column('soc_status', db.Enum("A", "I"))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
    

class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column('id', db.Integer, primary_key = True)
    log_id = db.Column('log_id', db.Integer)
    log_status = db.Column('log_status',db.Enum('non traitée', 'en cours de traitement', 'cloturée'), default='non traitée')
    log_category = db.Column(db.Enum('accéder', 'modifier', 'supprimer'))
    log_date = db.Column(db.DateTime(), default= str(datetime.now()))
    log_siret = db.Column('log_siret', db.BigInteger())
    log_society_name = db.Column('log_society_name', db.String(400))
    log_admin_id = db.Column('log_admin_id', db.Integer, db.ForeignKey('users.user_id'))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
