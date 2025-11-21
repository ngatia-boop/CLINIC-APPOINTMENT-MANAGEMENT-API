import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Allow all origins for now — we will restrict later on Render
CORS(app, resources={r"/*": {"origins": "*"}})

# -----------------------------
# IN-MEMORY "DATABASE"
# -----------------------------
patients = []
doctors = []
appointments = []


@app.route("/", strict_slashes=False)
def home():
    return jsonify({"message": "Clinic API running!"})


# -----------------------------
# PATIENTS ENDPOINT
# -----------------------------
@app.route("/patients", methods=["GET", "POST"], strict_slashes=False)
def patients_handler():
    if request.method == "GET":
        return jsonify(patients)

    data = request.get_json()
    patients.append(data)
    return jsonify(data), 201


# -----------------------------
# DOCTORS ENDPOINT
# -----------------------------
@app.route("/doctors", methods=["GET", "POST"], strict_slashes=False)
def doctors_handler():
    if request.method == "GET":
        return jsonify(doctors)

    data = request.get_json()
    doctors.append(data)
    return jsonify(data), 201


# -----------------------------
# APPOINTMENTS ENDPOINT
# -----------------------------
@app.route("/appointments", methods=["GET", "POST"], strict_slashes=False)
def appointments_handler():
    if request.method == "GET":
        return jsonify(appointments)

    data = request.get_json()
    appointments.append(data)
    return jsonify(data), 201


# -----------------------------
# RENDER DEPLOYMENT ENTRYPOINT
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5555))  # Render gives its own port
    app.run(host="0.0.0.0", port=port, debug=False)
