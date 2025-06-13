from flask import Flask, request, jsonify
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mariadb"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "example"),
        database=os.getenv("DB_NAME", "testdb")
    )

@app.route("/comments", methods=["GET"])
def get_comments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, comment FROM comments ORDER BY id DESC")
        comments = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify([{"name": n, "comment": c} for n, c in comments])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/comments", methods=["POST"])
def post_comment():
    data = request.get_json()
    name = data.get("name")
    comment = data.get("comment")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comments (name, comment) VALUES (%s, %s)", (name, comment))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Comentario guardado exitosamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
