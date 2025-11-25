# backend/main.py
from flask import Flask, jsonify, request
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["*"])  # Allow all origins for now


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5555, debug=True)