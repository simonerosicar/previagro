import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configurações base"""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///previagro.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-secret-key-please-change-this-to-a-secure-value-12345",
    )
    JWT_SECRET_KEY = os.environ.get(
        "JWT_SECRET_KEY",
        "dev-jwt-secret-key-please-change-this-to-a-secure-value-67890",
    )
    JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", 86400))
    AUTH_USERNAME = os.environ.get("AUTH_USERNAME", "admin")
    AUTH_PASSWORD = os.environ.get("AUTH_PASSWORD", "senha123")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

class DevelopmentConfig(Config):
    """Ambiente de desenvolvimento"""

    DEBUG = True

class ProductionConfig(Config):
    """Ambiente de produção"""

    DEBUG = False
    