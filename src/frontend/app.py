from flask import Flask, request
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

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        comment = request.form.get("comment")
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO comments (name, comment) VALUES (%s, %s)", (name, comment))
            conn.commit()
            cursor.close()
            conn.close()
            message = "Comentario guardado exitosamente."
        except Exception as e:
            message = f"Error al guardar comentario: {str(e)}"

    # Fetch comments
    comments = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, comment FROM comments ORDER BY id DESC")
        comments = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        comments = []

    comment_list = "<ul>" + "".join(f"<li><b>{n}</b>: {c}</li>" for n, c in comments) + "</ul>"

    return '''
    <html>
    <head><title>Comentarios</title></head>
    <body>
        <h1>Enviar Comentario</h1>
        <form method="POST">
            Nombre: <input name="name" /><br/>
            Comentario: <input name="comment" /><br/>
            <button type="submit">Enviar</button>
        </form>
        <p>{message}</p>
        <h2>Comentarios Previos</h2>
        {comments}
    </body>
    </html>
    '''.format(message=message, comments=comment_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
