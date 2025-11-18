# backend/routes/doctor_routes.py

from flask_restful import Resource
from flask import request
from ..extensions import db, api
from ..models import Doctor, Service

def serialize_doctor(doctor):
    return {
        'id': doctor.id,
        'first_name': doctor.first_name,
        'last_name': doctor.last_name,
        'specialty': doctor.specialty,
        'phone': doctor.phone,
        'services': [{'id': s.id, 'name': s.name} for s in doctor.services]
    }

class DoctorList(Resource):
    def get(self):
        doctors = Doctor.query.all()
        return [serialize_doctor(d) for d in doctors], 200

    def post(self):
        data = request.get_json()
        service_ids = data.pop('service_ids', [])
        try:
            new_doctor = Doctor(
                first_name=data['first_name'],
                last_name=data['last_name'],
                specialty=data['specialty'],
                phone=data.get('phone')
            )
            if service_ids:
                services = Service.query.filter(Service.id.in_(service_ids)).all()
                if len(services) != len(service_ids):
                    db.session.rollback()
                    return {'message': 'One or more service IDs are invalid.'}, 400
                new_doctor.services.extend(services)
            db.session.add(new_doctor)
            db.session.commit()
            return serialize_doctor(new_doctor), 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

class DoctorDetail(Resource):
    def get(self, id):
        doctor = Doctor.query.get_or_404(id)
        return serialize_doctor(doctor), 200

    def patch(self, id):
        doctor = Doctor.query.get_or_404(id)
        data = request.get_json()
        service_ids = data.pop('service_ids', None)
        try:
            for key, value in data.items():
                if hasattr(doctor, key):
                    setattr(doctor, key, value)
            if service_ids is not None:
                services = Service.query.filter(Service.id.in_(service_ids)).all()
                if len(services) != len(service_ids):
                    db.session.rollback()
                    return {'message': 'Invalid service IDs.'}, 400
                doctor.services = services
            db.session.commit()
            return serialize_doctor(doctor), 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

    def delete(self, id):
        doctor = Doctor.query.get_or_404(id)
        try:
            db.session.delete(doctor)
            db.session.commit()
            return {'message': 'Doctor deleted successfully'}, 204
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

api.add_resource(DoctorList, '/doctors')
api.add_resource(DoctorDetail, '/doctors/<int:id>')
