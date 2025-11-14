from flask import Blueprint, request, jsonify
from backend import db
from backend.models.patient import Patient

patient_bp = Blueprint('patient_bp', __name__)

def error_response(message, status=400):
    return jsonify({'error': message}), status

# GET /patients/ → list all patients
@patient_bp.route('/', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([p.to_dict() for p in patients]), 200

# POST /patients/ → create a new patient
@patient_bp.route('/', methods=['POST'])
def create_patient():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    if not name or not email:
        return error_response('name and email are required')

    # check for email uniqueness
    if Patient.query.filter_by(email=email).first():
        return error_response('email already exists')

    try:
        p = Patient(name=name, email=email, phone=phone)
        db.session.add(p)
        db.session.commit()
        return jsonify(p.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), 500)

# GET /patients/<id> → get a single patient
@patient_bp.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    p = Patient.query.get_or_404(patient_id)
    return jsonify(p.to_dict()), 200
