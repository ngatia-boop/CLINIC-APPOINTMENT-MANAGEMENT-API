# backend/seed.py

import os
from datetime import datetime, timedelta
from .app import create_app
from .extensions import db
from .models import Patient, Doctor, Appointment, Service

# Set the environment (Flask config)
app = create_app('development')

def seed_db():
    with app.app_context():
        print("Starting database seeding...")

        # --- Services ---
        services_data = [
            {"name": "General Checkup", "duration_minutes": 30, "price": 80.0},
            {"name": "Dental Cleaning", "duration_minutes": 60, "price": 150.0},
            {"name": "Physical Therapy", "duration_minutes": 45, "price": 100.0},
        ]

        for s in services_data:
            service = Service.query.filter_by(name=s['name']).first()
            if not service:
                db.session.add(Service(**s))
        db.session.commit()
        print("Services seeded.")

        # --- Doctors ---
        doctors_data = [
            {"first_name": "Alice", "last_name": "Smith", "specialty": "General Practice", "phone": "555-0001", "service_names": ["General Checkup", "Physical Therapy"]},
            {"first_name": "Bob", "last_name": "Jones", "specialty": "Dentistry", "phone": "555-0002", "service_names": ["Dental Cleaning"]},
            {"first_name": "Carol", "last_name": "Lee", "specialty": "Physiotherapy", "phone": "555-0003", "service_names": ["Physical Therapy"]},
        ]

        for d in doctors_data:
            doctor = Doctor.query.filter_by(first_name=d['first_name'], last_name=d['last_name']).first()
            if not doctor:
                doctor_services = Service.query.filter(Service.name.in_(d['service_names'])).all()
                doctor = Doctor(
                    first_name=d['first_name'],
                    last_name=d['last_name'],
                    specialty=d['specialty'],
                    phone=d['phone']
                )
                doctor.services.extend(doctor_services)
                db.session.add(doctor)
        db.session.commit()
        print("Doctors seeded and linked to services.")

        # --- Patients ---
        patients_data = [
            {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone": "555-1001"},
            {"first_name": "Jane", "last_name": "Avery", "email": "jane.avery@example.com", "phone": "555-1002"},
        ]

        for p in patients_data:
            patient = Patient.query.filter_by(email=p['email']).first()
            if not patient:
                db.session.add(Patient(**p))
        db.session.commit()
        print("Patients seeded.")

        # --- Appointments ---
        now = datetime.utcnow()

        # Appointment list with patient email and doctor name to avoid duplicates
        appointments_data = [
            {
                "patient_email": "john.doe@example.com",
                "doctor_name": ("Alice", "Smith"),
                "service_name": "General Checkup",
                "start_offset": timedelta(days=1, hours=10),
                "status": "Scheduled"
            },
            {
                "patient_email": "jane.avery@example.com",
                "doctor_name": ("Bob", "Jones"),
                "service_name": "Dental Cleaning",
                "start_offset": timedelta(days=1, hours=14),
                "status": "Scheduled"
            },
            {
                "patient_email": "john.doe@example.com",
                "doctor_name": ("Alice", "Smith"),
                "service_name": "Physical Therapy",
                "start_offset": timedelta(days=1, hours=11),
                "status": "Completed"
            }
        ]

        for a in appointments_data:
            patient = Patient.query.filter_by(email=a['patient_email']).first()
            doctor = Doctor.query.filter_by(first_name=a['doctor_name'][0], last_name=a['doctor_name'][1]).first()
            service = Service.query.filter_by(name=a['service_name']).first()

            start_time = now.replace(minute=0, second=0, microsecond=0) + a['start_offset']
            end_time = start_time + timedelta(minutes=service.duration_minutes)

            # Skip if an appointment with same patient, doctor, service, start_time exists
            existing_appt = Appointment.query.filter_by(
                patient_id=patient.id,
                doctor_id=doctor.id,
                service_id=service.id,
                start_time=start_time
            ).first()
            if not existing_appt:
                new_appt = Appointment(
                    patient_id=patient.id,
                    doctor_id=doctor.id,
                    service_id=service.id,
                    start_time=start_time,
                    end_time=end_time,
                    status=a['status']
                )
                db.session.add(new_appt)
        db.session.commit()
        print("Appointments seeded.")

        print("Database seeding complete!")

if __name__ == '__main__':
    seed_db()
