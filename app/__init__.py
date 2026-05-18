import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException, Unauthorized

from config import DevelopmentConfig
from app.routes import register_routes
from app.utils.exceptions import AuthenticationError, ValidationError


db = SQLAlchemy()
jwt = JWTManager()


def configure_logging(app):
    logs_path = Path(app.root_path).parent / "logs"
    logs_path.mkdir(exist_ok=True)

    handler = RotatingFileHandler(
        logs_path / "previagro.log",
        maxBytes=1024 * 1024,
        backupCount=3,
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] %(message)s"
        )
    )
    handler.setLevel(app.config["LOG_LEVEL"])
    app.logger.setLevel(app.config["LOG_LEVEL"])
    app.logger.addHandler(handler)
    app.logger.propagate = False


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        app.logger.warning("Validation error: %s", error.message)
        return jsonify({"erro": error.message}), 400

    @app.errorhandler(AuthenticationError)
    def handle_auth_error(error):
        app.logger.warning("Authentication error: %s", error.message)
        return jsonify({"erro": error.message}), 401

    @app.errorhandler(Unauthorized)
    def handle_unauthorized(error):
        app.logger.warning("Unauthorized: %s", error.description)
        return jsonify({"erro": error.description}), error.code

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        app.logger.warning("HTTP exception: %s", error.description)
        return jsonify({"erro": error.description}), error.code

    @app.errorhandler(Exception)
    def handle_exception(error):
        app.logger.exception(error)
        return jsonify({"erro": "Erro interno do servidor"}), 500


def register_jwt_callbacks(app):
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        app.logger.warning("JWT token expired")
        return jsonify({"erro": "Token expirado"}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error_string):
        app.logger.warning("JWT invalid token: %s", error_string)
        return jsonify({"erro": "Token inválido"}), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error_string):
        app.logger.warning("JWT missing token: %s", error_string)
        return jsonify({"erro": error_string}), 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        app.logger.warning("JWT revoked token")
        return jsonify({"erro": "Token revogado"}), 401


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    configure_logging(app)
    register_error_handlers(app)

    db.init_app(app)
    jwt.init_app(app)
    register_jwt_callbacks(app)

    with app.app_context():
        from app.models import Produtor, User

        db.create_all()

    register_routes(app)

    @app.before_request
    def log_request():
        app.logger.info("%s %s", request.method, request.path)

    return app