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
    SQLALCHEMY_DATABASE_URI = 'postgres://dqymjvexvlkdnu:cd96a74c6402bad8fb1fa0c96de4a93782fcc65c293f6f20fa9f0fd958547f4c@ec2-54-209-221-231.compute-1.amazonaws.com:5432/de7rsdpmpu2c42'
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