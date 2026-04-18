import hashlib
import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fixed: load secret/API key from environment variable
API_KEY = os.getenv("DEMO_API_KEY", "demo-key-not-set")

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

    # Fixed: use SHA-256 instead of MD5
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    users[username] = password_hash

    return jsonify({"message": "user registered", "user": username})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username', '')
    password = data.get('password', '')

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == password_hash:
        return jsonify({"message": "login success", "api_key_configured": API_KEY != 'demo-key-not-set'})
    return jsonify({"error": "invalid credentials"}), 401

@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')

    # Fixed: avoid shell=True and pass args safely
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    return f"<pre>{result.stdout or result.stderr}</pre>"

if __name__ == '__main__':
    # Fixed: debug disabled
    app.run(host='0.0.0.0', port=5000, debug=False)
