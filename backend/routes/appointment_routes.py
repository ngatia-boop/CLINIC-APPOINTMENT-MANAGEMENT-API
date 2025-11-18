# backend/routes/appointment_routes.py

from flask_restful import Resource
from flask import request
from ..extensions import db, api
from ..models import Appointment, Service, Doctor
from datetime import datetime, timedelta

# Serializer helper
def serialize_appointment(appointment):
    return {
        'id': appointment.id,
        'patient_id': appointment.patient_id,
        'doctor_id': appointment.doctor_id,
        'service_id': appointment.service_id,
        'start_time': appointment.start_time.isoformat(),
        'end_time': appointment.end_time.isoformat(),
        'status': appointment.status,
        'doctor_name': f"{appointment.doctor.first_name} {appointment.doctor.last_name}",
        'service_name': appointment.service.name
    }

# Resource for listing and creating appointments
class AppointmentList(Resource):
    def get(self):
        appointments = Appointment.query.all()
        return [serialize_appointment(a) for a in appointments], 200

    def post(self):
        data = request.get_json()
        doctor_id = data.get('doctor_id')
        service_id = data.get('service_id')
        start_time_str = data.get('start_time')

        if not all([doctor_id, service_id, start_time_str]):
            return {'message': 'Missing required fields: doctor_id, service_id, start_time'}, 400

        try:
            start_time = datetime.fromisoformat(start_time_str)
        except ValueError:
            return {'message': 'Invalid start_time format. Use ISO 8601.'}, 400

        service = Service.query.get(service_id)
        if not service:
            return {'message': f'Service with id {service_id} not found.'}, 404

        end_time = start_time + timedelta(minutes=service.duration_minutes)

        overlapping_appt = Appointment.query.filter(
            Appointment.doctor_id == doctor_id,
            Appointment.status == 'Scheduled',
            Appointment.start_time < end_time,
            Appointment.end_time > start_time
        ).first()

        if overlapping_appt:
            return {'message': 'Doctor is not available at this time. Overlaps with existing appointment.',
                    'overlapping_id': overlapping_appt.id}, 409

        try:
            new_appointment = Appointment(
                patient_id=data['patient_id'],
                doctor_id=doctor_id,
                service_id=service_id,
                start_time=start_time,
                end_time=end_time,
                status=data.get('status', 'Scheduled')
            )
            db.session.add(new_appointment)
            db.session.commit()
            return serialize_appointment(new_appointment), 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

# Resource for individual appointments
class AppointmentDetail(Resource):
    def get(self, id):
        appointment = Appointment.query.get_or_404(id)
        return serialize_appointment(appointment), 200

    def patch(self, id):
        appointment = Appointment.query.get_or_404(id)
        data = request.get_json()

        if 'start_time' in data or 'doctor_id' in data:
            start_time = datetime.fromisoformat(data.get('start_time', appointment.start_time.isoformat()))
            doctor_id = data.get('doctor_id', appointment.doctor_id)
            end_time = start_time + timedelta(minutes=appointment.service.duration_minutes)

            overlapping_appt = Appointment.query.filter(
                Appointment.doctor_id == doctor_id,
                Appointment.status == 'Scheduled',
                Appointment.start_time < end_time,
                Appointment.end_time > start_time,
                Appointment.id != id
            ).first()

            if overlapping_appt:
                return {'message': 'Doctor is not available at this time.', 'overlapping_id': overlapping_appt.id}, 409

            appointment.start_time = start_time
            appointment.end_time = end_time
            appointment.doctor_id = doctor_id

        if 'status' in data:
            appointment.status = data['status']

        try:
            db.session.commit()
            return serialize_appointment(appointment), 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 400

    def delete(self, id):
        appointment = Appointment.query.get_or_404(id)
        db.session.delete(appointment)
        db.session.commit()
        return {'message': 'Appointment deleted successfully'}, 204

# Register Resources
api.add_resource(AppointmentList, '/appointments')
api.add_resource(AppointmentDetail, '/appointments/<int:id>')
