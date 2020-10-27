

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'mysql://lucas:Claus5991.@localhost/Manageo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = 300
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT =  587 
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_USERNAME  = 'lucas.deleage@gmail.com'
    MAIL_PASSWORD = 'claus5991'
    MAIL_DEFAULT_SENDER = ('Manageo.fr', 'fausse.addresse@gmail.com')
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

