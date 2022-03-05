# import warnings
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # ....
        # Initializing flask extensions
  
    # if (
    #         'SQLALCHEMY_DATABASE_URI' not in app.config and
    #         'SQLALCHEMY_BINDS' not in app.config
    #     ):
    #         warnings.warn(
    #             'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
    #             'Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".'
    #         )
    

    app.config.from_object(config_options[config_name])
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
   
    return app    