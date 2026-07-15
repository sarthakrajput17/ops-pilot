from flask import Flask
from routes import register_routes
from config import Config
from logger import logger

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

logger.info("Flask application started")

register_routes(app)


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.APP_PORT, debug=True)