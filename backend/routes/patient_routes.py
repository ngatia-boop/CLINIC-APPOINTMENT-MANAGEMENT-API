# backend/routes/patient_routes.py

from flask_restful import Resource
from flask import request
from ..extensions import db, api
from ..models import Patient

def serialize_patient(patient):
    return {
        'id': patient.id,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'email': patient.email,
        'phone': patient.phone
    }

class PatientList(Resource):
    def get(self):
        patients = Patient.query.all()
        return [serialize_patient(p) for p in patients], 200

    def post(self):
        data = request.get_json()
        try:
            new_patient = Patient(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data.get('phone')
            )
            db.session.add(new_patient)
            db.session.commit()
            return serialize_patient(new_patient), 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

class PatientDetail(Resource):
    def get(self, id):
        patient = Patient.query.get_or_404(id)
        return serialize_patient(patient), 200

    def patch(self, id):
        patient = Patient.query.get_or_404(id)
        data = request.get_json()
        try:
            for key, value in data.items():
                if hasattr(patient, key):
                    setattr(patient, key, value)
            db.session.commit()
            return serialize_patient(patient), 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

    def delete(self, id):
        patient = Patient.query.get_or_404(id)
        db.session.delete(patient)
        db.session.commit()
        return {'message': 'Patient deleted successfully'}, 204

api.add_resource(PatientList, '/patients')
api.add_resource(PatientDetail, '/patients/<int:id>')
