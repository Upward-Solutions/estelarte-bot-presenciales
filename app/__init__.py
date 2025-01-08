import os

from flask import Flask

from app.config import Config
from app.db import init_app
from app.routes import api
from app.ui import ui


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-por-defecto")
    init_app(app)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(ui, url_prefix="")

    return app
