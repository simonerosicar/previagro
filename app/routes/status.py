from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)


@status_bp.route("/")
def home():
    return "PREVIAGRO API ONLINE"


@status_bp.route("/api/status")
def status():
    return jsonify({"status": "online", "sistema": "PREVIAGRO", "versao": "1.0"})