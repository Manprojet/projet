from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from .models import User
import re


class registerForm(FlaskForm): #formulaire d'inscription

    email = StringField('Email', validators=[DataRequired(), Email(message = 'Adresse mail incorrecte')])
    first_name = StringField('First_name', validators=[DataRequired()])
    last_name = StringField('Last_name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Les mots de passe doivent être les mêmes'),Length(min=8, max=20, message = 'Le mot de passe doit contenir entre 8 et 20 caractères')])
    password_confirm = PasswordField('Password_confirm', validators=[DataRequired()])
    submit = SubmitField("S'inscrire")

    def validate_password(self, password): #verification mdp
        specialChars = re.compile('[@_!#$%^&*()<>?/\|}{~:.]') 
        if not any(c.isupper() for c in password.data) or not any(c.islower() for c in password.data) or not any(c.isnumeric() for c in password.data) or specialChars.search(password.data) == None:
            raise ValidationError('Le mot de passe doit contenir au moins une majuscule, une minuscule, un chiffre et un charactère spécial')
                   
    def validate_email(self, email): #verification doublon email bdd
        user = User.query.filter_by(user_email = email.data).first() 
        if user:
            raise ValidationError('Email déjà existant')


class loginForm(FlaskForm): #formulaire de connexion

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField("Se connecter")


class requestForm(FlaskForm):

    request =  SelectField('request', choices=[('accéder', "Demande d'accès"), ('supprimer', 'Demande de suppression'), ('modifier', 'Demande de modification')])  
    societyName = StringField('societyName', validators=[DataRequired()])
    siret = StringField('siret', validators=[DataRequired()])
    file = FileField('field')
    submit = SubmitField("Envoyer")





