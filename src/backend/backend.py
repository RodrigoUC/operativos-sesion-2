from flask import Flask
import datetime
import os
import mysql.connector

app = Flask(__name__)

@app.route("/data")
def get_data():
    now = datetime.datetime.now()
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mariadb"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "example"),
            database=os.getenv("DB_NAME", "testdb")
        )
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return {"message": "Hora del servidor DB:", "data": str(result[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
