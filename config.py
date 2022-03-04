import os


class config:
    """
        Config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiprono12@localhost/pitches'
class prodConfig(config):
    """ production configuration class child class
    """    
    pass
class devConfig(config):
    """ dev configuration class child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiprono12@localhost/pitches'
    DEBUG=True
config_options={
"production":prodConfig,
"development":devConfig
}    