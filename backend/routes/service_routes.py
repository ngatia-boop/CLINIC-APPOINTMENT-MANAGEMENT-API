# backend/routes/service_routes.py

from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from ..extensions import db, api
from ..models import Service

def serialize_service(service):
    return {
        'id': service.id,
        'name': service.name,
        'duration_minutes': service.duration_minutes,
        'price': service.price,
        'doctor_count': service.doctors.count()
    }

class ServiceList(Resource):
    def get(self):
        services = Service.query.all()
        return [serialize_service(s) for s in services], 200

    def post(self):
        data = request.get_json()
        if not all(k in data for k in ['name', 'duration_minutes', 'price']):
            return {'message': 'Missing required fields.'}, 400
        try:
            service = Service(
                name=data['name'],
                duration_minutes=data['duration_minutes'],
                price=data['price']
            )
            db.session.add(service)
            db.session.commit()
            return serialize_service(service), 201
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Service name must be unique.'}, 409
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

class ServiceDetail(Resource):
    def get(self, id):
        service = Service.query.get_or_404(id)
        return serialize_service(service), 200

    def patch(self, id):
        service = Service.query.get_or_404(id)
        data = request.get_json()
        try:
            for key, value in data.items():
                if hasattr(service, key):
                    setattr(service, key, value)
            db.session.commit()
            return serialize_service(service), 200
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Service name must be unique.'}, 409
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

    def delete(self, id):
        service = Service.query.get_or_404(id)
        if service.doctors.count() > 0:
            return {'message': 'Cannot delete: linked to doctors'}, 409
        if service.appointments.count() > 0:
            return {'message': 'Cannot delete: linked to appointments'}, 409
        db.session.delete(service)
        db.session.commit()
        return {'message': 'Service deleted successfully'}, 204

api.add_resource(ServiceList, '/services')
api.add_resource(ServiceDetail, '/services/<int:id>')
