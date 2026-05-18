def register_routes(app):
    from app.routes.auth import auth_bp
    from app.routes.produtores import produtores_bp
    from app.routes.status import status_bp

    app.register_blueprint(status_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(produtores_bp)
