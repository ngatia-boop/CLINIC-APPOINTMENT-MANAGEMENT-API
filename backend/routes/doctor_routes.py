from flask import request, jsonify
from backend.models import Doctor
from backend.extensions import db
from backend.routes import doctors_bp

# GET all doctors
@doctors_bp.get("/")
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([d.to_dict() for d in doctors]), 200

# GET single doctor
@doctors_bp.get("/<int:id>")
def get_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    return jsonify(doctor.to_dict(include_appointments=True)), 200

# CREATE doctor
@doctors_bp.post("/")
def create_doctor():
    data = request.json
    doctor = Doctor(
        name=data["name"],
        specialization=data["specialization"],
        phone=data["phone"]
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify(doctor.to_dict()), 201

# UPDATE doctor
@doctors_bp.put("/<int:id>")
def update_doctor(id):
    data = request.json
    doctor = Doctor.query.get_or_404(id)

    doctor.name = data.get("name", doctor.name)
    doctor.specialization = data.get("specialization", doctor.specialization)
    doctor.phone = data.get("phone", doctor.phone)

    db.session.commit()
    return jsonify(doctor.to_dict()), 200

# DELETE doctor
@doctors_bp.delete("/<int:id>")
def delete_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    db.session.delete(doctor)
    db.session.commit()
    return jsonify({"message": "Doctor deleted"}), 200
