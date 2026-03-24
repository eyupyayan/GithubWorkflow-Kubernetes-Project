from flask import Blueprint, jsonify, request, current_app, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.storage import TaskStorage
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY, TASKS_CREATED
import time

bp = Blueprint("routes", __name__)
storage = TaskStorage()


@bp.route("/", methods=["GET"])
def index():
    start = time.time()

    response_body = {
        "message": "Task service is running",
        "app_name": current_app.config["APP_NAME"],
        "environment": current_app.config["APP_ENV"]
    }

    REQUEST_COUNT.labels(method="GET", endpoint="/", status="200").inc()
    REQUEST_LATENCY.labels(method="GET", endpoint="/").observe(time.time() - start)

    return jsonify(response_body)


@bp.route("/health", methods=["GET"])
def health():
    start = time.time()

    REQUEST_COUNT.labels(method="GET", endpoint="/health", status="200").inc()
    REQUEST_LATENCY.labels(method="GET", endpoint="/health").observe(time.time() - start)

    return jsonify({"status": "ok"}), 200


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    start = time.time()

    data = storage.list_tasks()

    REQUEST_COUNT.labels(method="GET", endpoint="/tasks", status="200").inc()
    REQUEST_LATENCY.labels(method="GET", endpoint="/tasks").observe(time.time() - start)

    return jsonify(data)


@bp.route("/tasks", methods=["POST"])
def create_task():
    start = time.time()

    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title:
        REQUEST_COUNT.labels(method="POST", endpoint="/tasks", status="400").inc()
        REQUEST_LATENCY.labels(method="POST", endpoint="/tasks").observe(time.time() - start)
        return jsonify({"error": "Field 'title' is required"}), 400

    task = storage.add_task(title)
    TASKS_CREATED.inc()

    REQUEST_COUNT.labels(method="POST", endpoint="/tasks", status="201").inc()
    REQUEST_LATENCY.labels(method="POST", endpoint="/tasks").observe(time.time() - start)

    return jsonify(task), 201


@bp.route("/metrics", methods=["GET"])
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)