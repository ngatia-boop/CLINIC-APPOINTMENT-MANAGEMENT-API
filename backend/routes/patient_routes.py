from flask import request, jsonify
from backend.models import Patient
from backend.extensions import db
from backend.routes import patients_bp

@patients_bp.get("/")
def get_patients():
    patients = Patient.query.all()
    return jsonify([p.to_dict() for p in patients]), 200

@patients_bp.get("/<int:id>")
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient.to_dict(include_appointments=True)), 200

@patients_bp.post("/")
def create_patient():
    data = request.json
    patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data["gender"],
        phone=data["phone"]
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient.to_dict()), 201

@patients_bp.put("/<int:id>")
def update_patient(id):
    data = request.json
    patient = Patient.query.get_or_404(id)
    patient.name = data.get("name", patient.name)
    patient.age = data.get("age", patient.age)
    patient.gender = data.get("gender", patient.gender)
    patient.phone = data.get("phone", patient.phone)
    db.session.commit()
    return jsonify(patient.to_dict()), 200

@patients_bp.delete("/<int:id>")
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted"}), 200
