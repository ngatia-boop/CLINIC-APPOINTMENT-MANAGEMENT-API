# backend/main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

patients, doctors, appointments = [], [], []

# -- PATIENTS --
@app.route("/patients/", methods=["GET", "POST"])
def patients_list():
    if request.method == "GET":
        return jsonify(patients)
    data = request.json
    new_patient = {"id": len(patients)+1, **data}
    patients.append(new_patient)
    return jsonify(new_patient), 201

@app.route("/patients/<int:id>", methods=["GET", "PATCH", "DELETE"])
def patient_detail(id):
    patient = next((p for p in patients if p["id"] == id), None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if request.method == "PATCH":
        patient.update(request.json)
    if request.method == "DELETE":
        patients.remove(patient)
        return jsonify({"message": "Patient deleted"})
    return jsonify(patient)

# -- DOCTORS --
@app.route("/doctors/", methods=["GET", "POST"])
def doctors_list():
    if request.method == "GET":
        return jsonify(doctors)
    data = request.json
    new_doctor = {"id": len(doctors)+1, **data}
    doctors.append(new_doctor)
    return jsonify(new_doctor), 201

@app.route("/doctors/<int:id>", methods=["GET", "PATCH", "DELETE"])
def doctor_detail(id):
    doctor = next((d for d in doctors if d["id"] == id), None)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404
    if request.method == "PATCH":
        doctor.update(request.json)
    if request.method == "DELETE":
        doctors.remove(doctor)
        return jsonify({"message": "Doctor deleted"})
    return jsonify(doctor)

# -- APPOINTMENTS --
@app.route("/appointments/", methods=["GET", "POST"])
def appointments_list():
    if request.method == "GET":
        return jsonify(appointments)
    data = request.json
    new_appt = {"id": len(appointments)+1, **data}
    appointments.append(new_appt)
    return jsonify(new_appt), 201

@app.route("/appointments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def appointment_detail(id):
    appt = next((a for a in appointments if a["id"] == id), None)
    if not appt:
        return jsonify({"error": "Appointment not found"}), 404
    if request.method == "PATCH":
        appt.update(request.json)
    if request.method == "DELETE":
        appointments.remove(appt)
        return jsonify({"message": "Appointment deleted"})
    return jsonify(appt)

@app.route("/")
def home():
    return jsonify({"message": "Clinic Appointment API is running!"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
