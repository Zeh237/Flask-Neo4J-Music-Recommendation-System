import os
from decouple import config
from flask import Flask, render_template
from flask_avatars import Avatars
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache



app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

db = SQLAlchemy(app)

app.config['SESSION_SQLALCHEMY'] = db

moment = Moment(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

avatars = Avatars(app)

cache = Cache(app)






# from src.api.routes import api

# Registering blueprints
# app.register_blueprint(website, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/auth/')
# app.register_blueprint(api, url_prefix='/api/')

# schedule_tasks()
