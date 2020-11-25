from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#initilizing application
app = Flask(__name__)


#seting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


#intializing Flask Extentions
bootstrap = Bootstrap(app)


from app import views