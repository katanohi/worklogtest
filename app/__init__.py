from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes.auth import auth_bp

db: SQLAlchemy = SQLAlchemy()


def create_app(config_name: str) -> Flask:
    """アプリ作成用ファクトリ"""

    app: Flask = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint(auth_bp)
    db.init_app(app)

    return app
