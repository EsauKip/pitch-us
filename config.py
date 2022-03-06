import os


class config:
    """
        Config
    """
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='iamkip'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiprono12@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
class prodConfig(config):
    """ production configuration class child class
    """    
    pass
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