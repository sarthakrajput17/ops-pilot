from flask import Flask
from routes import register_routes
from config import Config

app = Flask(__name__)
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.APP_PORT, debug=True)