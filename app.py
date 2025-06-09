from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    users.append({"username": data.get("username")})
    return jsonify({"message": "Kayıt başarılı"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
