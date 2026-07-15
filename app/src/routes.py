from flask import request, jsonify
from logger import logger
from db import (
    get_db_connection,
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)


def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():

        try:
            conn = get_db_connection()
            conn.close()

            logger.info("GET /health - Database connection successful")

            return jsonify({
                "status": "ok",
                "database": "connected"
            })

        except Exception as e:
            logger.error(f"GET /health - Database connection failed: {str(e)}")
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500


    @app.route("/users", methods=["POST"])
    def add_user():

        data = request.get_json()

        if data is None:
            return jsonify({
                "message": "Request body is required"
            }), 400

        name = data.get("name")
        email = data.get("email")

        if not name:
            return jsonify({
                "message": "Name is required"
            }), 400

        if not email:
            return jsonify({
                "message": "Email is required"
            }), 400

        try:
           user_id = create_user(name, email)

           return jsonify({
              "message": "User created successfully",
              "id": user_id
            }), 201

        except ValueError as e:
            return jsonify({
               "message": str(e)
            }), 409
    
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
    
    @app.route("/users/<int:user_id>", methods=["PUT"])
    def update_existing_user(user_id):

        data = request.get_json()

        name = data["name"]
        email = data["email"]

        updated_rows = update_user(user_id, name, email)

        if updated_rows == 0:
            return jsonify({
            "message": "User not found"
            }), 404

        return jsonify({
            "message": "User updated successfully"
        }), 200
    
    @app.route("/users/<int:user_id>", methods=["DELETE"])
    def remove_user(user_id):

        deleted_rows = delete_user(user_id)

        if deleted_rows == 0:
             return jsonify({
                 "message": "User not found"
            }), 404

        return jsonify({
            "message": "User deleted successfully"
        }), 200