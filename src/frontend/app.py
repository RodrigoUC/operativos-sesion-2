from flask import Flask, request
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5001")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        comment = request.form.get("comment")
        try:
            response = requests.post(f"{BACKEND_URL}/comments", json={"name": name, "comment": comment})
            if response.status_code == 200:
                message = "Comentario enviado exitosamente."
            else:
                message = f"Error desde backend: {response.text}"
        except Exception as e:
            message = f"Error al contactar backend: {e}"

    # Obtener comentarios
    comments = []
    try:
        response = requests.get(f"{BACKEND_URL}/comments")
        if response.status_code == 200:
            comments = response.json()
    except:
        comments = []

    comment_list = "<ul>" + "".join(f"<li><b>{c['name']}</b>: {c['comment']}</li>" for c in comments) + "</ul>"

    return f'''
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
        {comment_list}
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
