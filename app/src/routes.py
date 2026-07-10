from flask import jsonify
from db import get_db_connection

def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():
        try:
            conn = get_db_connection()
            conn.close()
            return jsonify({
                "status": "ok",
                "database": "connected"
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "database": "disconnected",
                "message": str(e)
            }), 500