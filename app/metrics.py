from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "task_service_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "task_service_http_request_duration_seconds",
    "HTTP request latency",
    ["method", "endpoint"]
)

TASKS_CREATED = Counter(
    "task_service_tasks_created_total",
    "Total created tasks"
)