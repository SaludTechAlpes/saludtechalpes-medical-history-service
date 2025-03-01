from flask import Flask
from src.config.config import Config
config = Config()

def create_app(configuration=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/health")
    def health():
        return {
            "status": "up",
            "application_name": config.APP_NAME,
            "environment": config.ENVIRONMENT
        }
    
    return app