import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "task-service")
    APP_ENV = os.getenv("APP_ENV", "dev")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")