import os

os.environ["FLASK_ENV"] = "development"
os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = "test-secret-123456789012345678901234567890"
os.environ["JWT_SECRET_KEY"] = "test-secret-123456789012345678901234567890"

from app import create_app, db


def create_test_app():
    app = create_app()
    app.testing = True
    with app.app_context():
        db.create_all()
    return app


def test_auth_register_and_login():
    app = create_test_app()
    client = app.test_client()

    rv = client.post(
        "/api/auth/register",
        json={"username": "testuser", "password": "senha123"},
    )
    assert rv.status_code == 201
    assert rv.get_json()["usuario"]["username"] == "testuser"

    rv = client.post(
        "/api/auth/login",
        json={"username": "testuser", "password": "senha123"},
    )
    assert rv.status_code == 200
    login_data = rv.get_json()
    assert "access_token" in login_data
    assert "refresh_token" in login_data


def test_auth_login_invalid_credentials_returns_401():
    app = create_test_app()
    client = app.test_client()

    rv = client.post(
        "/api/auth/login",
        json={"username": "wronguser", "password": "wrongpass"},
    )
    assert rv.status_code == 401
    assert "erro" in rv.get_json()


def test_produtor_crud_with_jwt():
    app = create_test_app()
    client = app.test_client()

    rv = client.post(
        "/api/auth/register",
        json={"username": "testuser", "password": "senha123"},
    )
    assert rv.status_code == 201

    rv = client.post(
        "/api/auth/login",
        json={"username": "testuser", "password": "senha123"},
    )
    access_token = rv.get_json()["access_token"]

    rv = client.post(
        "/api/produtores",
        json={"nome": "João", "cidade": "São Paulo"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert rv.status_code == 201
    produtor_id = rv.get_json()["produtor"]["id"]

    rv = client.put(
        f"/api/produtores/{produtor_id}",
        json={"nome": "João Silva", "cidade": "Campinas", "ativo": False},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert rv.status_code == 200
    assert rv.get_json()["produtor"]["nome"] == "João Silva"

    rv = client.get("/api/produtores")
    assert rv.status_code == 200
    assert len(rv.get_json()) == 1

    rv = client.delete(
        f"/api/produtores/{produtor_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert rv.status_code == 200


def test_produtores_requires_jwt_token():
    app = create_test_app()
    client = app.test_client()

    rv = client.post(
        "/api/produtores",
        json={"nome": "João", "cidade": "São Paulo"},
    )
    assert rv.status_code == 401
    assert "erro" in rv.get_json()


def test_produtores_rejects_invalid_jwt_token():
    app = create_test_app()
    client = app.test_client()

    rv = client.post(
        "/api/produtores",
        json={"nome": "João", "cidade": "São Paulo"},
        headers={"Authorization": "Bearer invalid.token.value"},
    )
    assert rv.status_code == 401
    assert "erro" in rv.get_json()


def test_produtores_public_read_only():
    app = create_test_app()
    client = app.test_client()

    rv = client.get("/api/produtores")
    assert rv.status_code == 200
    assert isinstance(rv.get_json(), list)
