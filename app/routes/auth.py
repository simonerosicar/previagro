from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from werkzeug.exceptions import Unauthorized

from app.services.user_service import authenticate_user, create_user
from app.utils.validation import validate_login_payload, validate_user_payload

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/api/auth/register", methods=["POST"])
def register():
    dados = request.get_json() or {}
    payload = validate_user_payload(dados)
    novo_usuario = create_user(
        username=payload["username"],
        password=payload["password"],
    )
    return (
        jsonify({
            "mensagem": "Usuário registrado com sucesso",
            "usuario": novo_usuario.to_dict(),
        }),
        201,
    )


@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    dados = request.get_json() or {}
    credentials = validate_login_payload(dados)
    usuario = authenticate_user(
        username=credentials["username"], password=credentials["password"]
    )
    if usuario is None:
        raise Unauthorized("Usuário ou senha inválidos")

    access_token = create_access_token(identity=str(usuario.id))
    refresh_token = create_refresh_token(identity=str(usuario.id))

    return jsonify(
        {
            "mensagem": "Login efetuado com sucesso",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "usuario": {
                "id": usuario.id,
                "username": usuario.username,
            },
        }
    )


@auth_bp.route("/api/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify({"access_token": new_access_token})
