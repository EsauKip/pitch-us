import os

# app.config['SECRET_KEY'] ='iamkip'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://moringa:kiprono12@localhost/pitches'

class config:
    """
        Config
    """
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='iamkip'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiprono12@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class prodConfig():
    """ production configuration class child class
    """    
    SQLALCHEMY_DATABASE_URI = 'postgresql://mnciirajecbyku:33c8e4900cc8eded231eb4c14d1c825fbcc9c071c2f69a8056c06886f1238eb2@ec2-44-192-245-97.compute-1.amazonaws.com:5432/dcj2lj45iuek4c'
class devConfig(config):
    """ dev configuration class child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiprono12@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG=True
config_options={
"production":prodConfig,
"development":devConfig
}    