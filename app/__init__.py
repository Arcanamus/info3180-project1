from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(Config)
from app import views
from flask_migrate import Migrate
migrate = Migrate(app, db)