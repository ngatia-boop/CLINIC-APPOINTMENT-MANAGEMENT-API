# backend/main.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes, allowing all origins and necessary headers
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)

# -------------------------------
# In-memory data storage
# -------------------------------
patients = []
doctors = []
appointments = []

# =====================================================
# PATIENTS
# =====================================================
@app.route("/patients/", methods=["GET", "POST"], strict_slashes=False)
def patients_list():
    if request.method == "GET":
        return jsonify(patients), 200

    if request.method == "POST":
        data = request.json
        new_patient = {
            "id": len(patients) + 1,
            "name": data.get("name"),
            "age": data.get("age"),
            "gender": data.get("gender"),
            "phone": data.get("phone")
        }
        patients.append(new_patient)
        return jsonify(new_patient), 201


@app.route("/patients/<int:id>", methods=["GET", "PATCH", "DELETE"], strict_slashes=False)
def patient_detail(id):
    patient = next((p for p in patients if p["id"] == id), None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    if request.method == "GET":
        return jsonify(patient), 200

    if request.method == "PATCH":
        data = request.json
        patient.update(data)
        return jsonify(patient), 200

    if request.method == "DELETE":
        patients.remove(patient)
        return jsonify({"message": "Patient deleted"}), 200


# =====================================================
# DOCTORS
# =====================================================
@app.route("/doctors/", methods=["GET", "POST"], strict_slashes=False)
def doctors_list():
    if request.method == "GET":
        return jsonify(doctors), 200

    if request.method == "POST":
        data = request.json
        new_doctor = {
            "id": len(doctors) + 1,
            "name": data.get("name"),
            "specialty": data.get("specialty"),
            "phone": data.get("phone")
        }
        doctors.append(new_doctor)
        return jsonify(new_doctor), 201


@app.route("/doctors/<int:id>", methods=["GET", "PATCH", "DELETE"], strict_slashes=False)
def doctor_detail(id):
    doctor = next((d for d in doctors if d["id"] == id), None)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    if request.method == "GET":
        return jsonify(doctor), 200

    if request.method == "PATCH":
        data = request.json
        doctor.update(data)
        return jsonify(doctor), 200

    if request.method == "DELETE":
        doctors.remove(doctor)
        return jsonify({"message": "Doctor deleted"}), 200


# =====================================================
# APPOINTMENTS
# =====================================================
@app.route("/appointments/", methods=["GET", "POST"], strict_slashes=False)
def appointments_list():
    if request.method == "GET":
        return jsonify(appointments), 200

    if request.method == "POST":
        data = request.json
        new_appointment = {
            "id": len(appointments) + 1,
            "patient_id": data.get("patient_id"),
            "doctor_id": data.get("doctor_id"),
            "date": data.get("date"),
            "time": data.get("time"),
            "notes": data.get("notes", "")
        }
        appointments.append(new_appointment)
        return jsonify(new_appointment), 201


@app.route("/appointments/<int:id>", methods=["GET", "PATCH", "DELETE"], strict_slashes=False)
def appointment_detail(id):
    appt = next((a for a in appointments if a["id"] == id), None)
    if not appt:
        return jsonify({"error": "Appointment not found"}), 404

    if request.method == "GET":
        return jsonify(appt), 200

    if request.method == "PATCH":
        data = request.json
        appt.update(data)
        return jsonify(appt), 200

    if request.method == "DELETE":
        appointments.remove(appt)
        return jsonify({"message": "Appointment deleted"}), 200


@app.route("/", strict_slashes=False)
def home():
    return jsonify({"message": "Clinic Appointment API is running!"}), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
