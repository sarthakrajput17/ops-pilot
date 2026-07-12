import psycopg2
from config import Config

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return conn

def create_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (name, email)
    )

    user_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return user_id

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, created_at
        FROM users
        ORDER BY id;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "created_at": str(row[3])
        })

    return users

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, email, created_at
        FROM users
        WHERE id = %s;
        """,
        (user_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "created_at": str(row[3])
    }

def update_user(user_id, name, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET name = %s,
            email = %s
        WHERE id = %s;
        """,
        (name, email, user_id)
    )

    updated_rows = cursor.rowcount

    conn.commit()

    cursor.close()
    conn.close()

    return updated_rows

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id = %s;
        """,
        (user_id,)
    )

    deleted_rows = cursor.rowcount

    conn.commit()

    cursor.close()
    conn.close()

    return deleted_rows