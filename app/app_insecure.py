from flask import Flask, request, jsonify
import hashlib
import subprocess

app = Flask(__name__)

# Intentional vulnerability: hardcoded secret/API key
API_KEY = "sk-demo-hardcoded-key-12345"

users = {}

@app.route('/')
def home():
    return "Person A demo app is running"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}
    username = data.get('username', '')
    password = data.get('password', '')

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    # Intentional vulnerability: weak hashing (MD5)
    password_hash = hashlib.md5(password.encode()).hexdigest()
    users[username] = password_hash

    return jsonify({"message": "user registered", "user": username})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username', '')
    password = data.get('password', '')

    password_hash = hashlib.md5(password.encode()).hexdigest()
    if users.get(username) == password_hash:
        return jsonify({"message": "login success", "api_key_preview": API_KEY[:10]})
    return jsonify({"error": "invalid credentials"}), 401

@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')

    # Intentional vulnerability: command injection via shell=True
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True, text=True)
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    # Intentional vulnerability: debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
