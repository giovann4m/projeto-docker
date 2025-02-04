from flask import Flask, jsonify
from database import connect_db

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API Flask rodando dentro do Docker!"})

@app.route("/db-test")
def test_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    conn.close()
    return jsonify({"db_time": result[0].strftime("%Y-%m-%d %H:%M:%S")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
