import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Allow all origins for now — we will restrict later on Render
CORS(app, resources={r"/*": {"origins": "*"}})

# -----------------------------
# IN-MEMORY "DATABASE"
# -----------------------------
patients = []        # <---- THIS is what was missing
appointments = []    # (optional, for later)

@app.route("/")
def home():
    return jsonify({"message": "Clinic API running!"})

@app.route("/patients", methods=["GET", "POST"])
def patients_handler():
    if request.method == "GET":
        return jsonify(patients)

    elif request.method == "POST":
        data = request.get_json()
        patients.append(data)
        return jsonify(data), 201

# Required for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5555))
    app.run(host="0.0.0.0", port=port, debug=False)
