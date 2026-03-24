from flask import Blueprint, jsonify, request, current_app
from app.storage import TaskStorage

bp = Blueprint("routes", __name__)
storage = TaskStorage()


@bp.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Task service is running",
        "app_name": current_app.config["APP_NAME"],
        "environment": current_app.config["APP_ENV"]
    })


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK, you are doing WELL;)"}), 200


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(storage.list_tasks())


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}

    title = data.get("title")
    if not title:
        return jsonify({"error": "Field 'title' is required"}), 400

    task = storage.add_task(title)
    return jsonify(task), 201