from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.produtor_service import (
    atualizar_produtor,
    criar_produtor,
    get_produtor_or_404,
    listar_produtores,
    remover_produtor,
)
from app.utils.validation import validate_produtor_payload

produtores_bp = Blueprint("produtores", __name__)


@produtores_bp.route("/api/produtores", methods=["GET"])
def listar_produtores_route():
    produtores = listar_produtores()
    return jsonify([produtor.to_dict() for produtor in produtores])


@produtores_bp.route("/api/produtores", methods=["POST"])
@jwt_required()
def criar_produtor_route():
    dados = request.get_json() or {}
    payload = validate_produtor_payload(dados)
    novo_produtor = criar_produtor(nome=payload["nome"], cidade=payload["cidade"])
    return (
        jsonify({
            "mensagem": "Produtor criado com sucesso",
            "produtor": novo_produtor.to_dict(),
        }),
        201,
    )


@produtores_bp.route("/api/produtores/<int:produtor_id>", methods=["GET"])
def get_produtor_route(produtor_id):
    produtor = get_produtor_or_404(produtor_id)
    return jsonify(produtor.to_dict())


@produtores_bp.route("/api/produtores/<int:produtor_id>", methods=["PUT"])
@jwt_required()
def atualizar_produtor_route(produtor_id):
    produtor = get_produtor_or_404(produtor_id)
    dados = request.get_json() or {}
    payload = validate_produtor_payload(dados, partial=False)
    atualizado = atualizar_produtor(
        produtor,
        nome=payload["nome"],
        cidade=payload["cidade"],
        ativo=payload["ativo"],
        partial=False,
    )
    return jsonify(
        {
            "mensagem": "Produtor atualizado com sucesso",
            "produtor": atualizado.to_dict(),
        }
    )


@produtores_bp.route("/api/produtores/<int:produtor_id>", methods=["PATCH"])
@jwt_required()
def patch_produtor_route(produtor_id):
    produtor = get_produtor_or_404(produtor_id)
    dados = request.get_json() or {}
    payload = validate_produtor_payload(dados, partial=True)
    atualizado = atualizar_produtor(
        produtor,
        nome=payload.get("nome"),
        cidade=payload.get("cidade"),
        ativo=payload.get("ativo"),
        partial=True,
    )
    return jsonify(
        {
            "mensagem": "Produtor parcialmente atualizado com sucesso",
            "produtor": atualizado.to_dict(),
        }
    )


@produtores_bp.route("/api/produtores/<int:produtor_id>", methods=["DELETE"])
@jwt_required()
def delete_produtor_route(produtor_id):
    produtor = get_produtor_or_404(produtor_id)
    remover_produtor(produtor)
    return jsonify({"mensagem": "Produtor removido com sucesso"}), 200
