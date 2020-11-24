from flask import Flask
from .config import DevConfig


#initilizing application
app = Flask(__name__)


#seting up configuration
app.config.from_object(DevConfig)


from app import views