# backend/main.py
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
CORS(app, resources={r"/*": {"origins": "*"}})  

# Ensure tables exist
with app.app_context():
    db.create_all()


# -----------------------------
# HOME
# -----------------------------
@app.route("/", strict_slashes=False)
def home():
    return jsonify({"message": "Clinic API running!"})


# -----------------------------
# PATIENTS ENDPOINT
# -----------------------------
@app.route("/patients", methods=["GET", "POST"], strict_slashes=False)
def patients_handler():
    if request.method == "GET":
        patients = Patient.query.all()
        return jsonify([p.to_dict(include_appointments=True) for p in patients])

    data = request.get_json()
    patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data["gender"],
        phone=data["phone"]
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient.to_dict()), 201


# -----------------------------
# DOCTORS ENDPOINT
# -----------------------------
@app.route("/doctors", methods=["GET", "POST"], strict_slashes=False)
def doctors_handler():
    if request.method == "GET":
        doctors = Doctor.query.all()
        return jsonify([d.to_dict(include_appointments=True) for d in doctors])

    data = request.get_json()
    doctor = Doctor(
        name=data["name"],
        specialization=data["specialization"],
        phone=data["phone"]
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify(doctor.to_dict()), 201


# -----------------------------
# APPOINTMENTS ENDPOINT
# -----------------------------
@app.route("/appointments", methods=["GET", "POST"], strict_slashes=False)
def appointments_handler():
    if request.method == "GET":
        appointments = Appointment.query.all()
        return jsonify([a.to_dict(include_patient=True, include_doctor=True) for a in appointments])

    data = request.get_json()
    # Parse date and time strings
    date_obj = datetime.strptime(data["date"], "%Y-%m-%d").date()
    time_obj = datetime.strptime(data["time"], "%H:%M").time()

    appointment = Appointment(
        date=date_obj,
        time=time_obj,
        notes=data["notes"],
        patient_id=data["patient_id"],
        doctor_id=data.get("doctor_id")  # Optional
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify(appointment.to_dict(include_patient=True, include_doctor=True)), 201


# -----------------------------
# RENDER DEPLOYMENT ENTRYPOINT
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5555))
    app.run(host="0.0.0.0", port=port, debug=False)
