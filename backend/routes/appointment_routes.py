# backend/routes/appointment_routes.py
from flask import request, jsonify
from ..models import Appointment
from ..extensions import db
from . import appointments_bp
from datetime import datetime

# GET all appointments
@appointments_bp.get("/")
def get_appointments():
    appts = Appointment.query.all()
    return jsonify([a.to_dict(include_patient=True, include_doctor=True) for a in appts]), 200

# GET single appointment
@appointments_bp.get("/<int:id>")
def get_appointment(id):
    appt = Appointment.query.get_or_404(id)
    return jsonify(appt.to_dict(include_patient=True, include_doctor=True)), 200

# CREATE appointment
@appointments_bp.post("/")
def create_appointment():
    data = request.json
    date = datetime.strptime(data["date"], "%Y-%m-%d").date()
    time = datetime.strptime(data["time"], "%H:%M").time()

    appt = Appointment(
        date=date,
        time=time,
        notes=data["notes"],
        patient_id=data["patient_id"],
        doctor_id=data.get("doctor_id")
    )

    db.session.add(appt)
    db.session.commit()
    return jsonify(appt.to_dict()), 201

# UPDATE appointment
@appointments_bp.put("/<int:id>")
def update_appointment(id):
    data = request.json
    appt = Appointment.query.get_or_404(id)

    if "date" in data:
        appt.date = datetime.strptime(data["date"], "%Y-%m-%d").date()

    if "time" in data:
        appt.time = datetime.strptime(data["time"], "%H:%M").time()

    appt.notes = data.get("notes", appt.notes)
    appt.patient_id = data.get("patient_id", appt.patient_id)
    appt.doctor_id = data.get("doctor_id", appt.doctor_id)

    db.session.commit()
    return jsonify(appt.to_dict()), 200

# DELETE appointment
@appointments_bp.delete("/<int:id>")
def delete_appointment(id):
    appt = Appointment.query.get_or_404(id)
    db.session.delete(appt)
    db.session.commit()
    return jsonify({"message": "Appointment deleted"}), 200
