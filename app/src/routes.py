from flask import request, jsonify
from db import (
    get_db_connection,
    create_user,
    get_all_users,
    get_user_by_id
)


def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():

        try:
            conn = get_db_connection()
            conn.close()

            return jsonify({
                "status": "ok",
                "database": "connected"
            })

        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500


    @app.route("/users", methods=["POST"])
    def add_user():

        data = request.get_json()

        name = data["name"]
        email = data["email"]

        user_id = create_user(name, email)

        return jsonify({
            "message": "User created successfully",
            "id": user_id
        }), 201
    
    @app.route("/users", methods=["GET"])
    def get_users():

        users = get_all_users()

        return jsonify(users), 200
    

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):

        user = get_user_by_id(user_id)

        if user is None:
            return jsonify({
                "message": "User not found"
            }), 404

        return jsonify(user), 200