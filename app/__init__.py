from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Cors = CORS(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)

from app import views