from flask import Blueprint, jsonify
from monitoring.metrics import get_metrics

api_bp = Blueprint("api", __name__)

@api_bp.route("/metrics", methods=["GET"])
def get_system_metrics():
    return jsonify(get_metrics())