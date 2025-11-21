# backend/seed.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import create_app
from backend.extensions import db
from backend.models import Patient, Doctor, Appointment
from datetime import date, time

app = create_app()

with app.app_context():
    print("🔥 Clearing old data...")
    # Delete appointments first to avoid foreign key errors
    Appointment.query.delete()
    Doctor.query.delete()
    Patient.query.delete()
    db.session.commit()

    print("🌱 Adding Doctors...")
    doctors = [
        Doctor(name="Dr. Sarah Kim", specialization="Cardiology", phone="0712345678"),
        Doctor(name="Dr. John Mwangi", specialization="Dermatology", phone="0798765432"),
        Doctor(name="Dr. Diana Kithinji", specialization="Psychologist", phone="0700987654"),
    ]
    db.session.add_all(doctors)
    db.session.commit()  # Commit first to generate IDs

    print("🌱 Adding Patients...")
    patients = [
        Patient(name="Alice Wanjiku", age=28, gender="Female", phone="0700001111"),
        Patient(name="Brian Otieno", age=34, gender="Male", phone="0700002222"),
        Patient(name="Charles Mwangi", age=45, gender="Male", phone="0700003333"),
        Patient(name="Diana Njeri", age=32, gender="Female", phone="0700004444"),
    ]
    db.session.add_all(patients)
    db.session.commit()  # Commit to generate IDs

    print("🌱 Adding Appointments...")
    appointments = [
        Appointment(
            date=date(2025, 11, 20),
            time=time(10, 30),
            notes="Routine checkup",
            patient_id=patients[0].id,
            doctor_id=doctors[0].id
        ),
        Appointment(
            date=date(2025, 11, 21),
            time=time(14, 15),
            notes="Skin rash treatment",
            patient_id=patients[1].id,
            doctor_id=doctors[1].id
        ),
        Appointment(
            date=date(2025, 11, 22),
            time=time(9, 0),
            notes="Psychology consultation",
            patient_id=patients[3].id,
            doctor_id=doctors[2].id
        ),
        Appointment(
            date=date(2025, 11, 23),
            time=time(11, 45),
            notes="Follow-up heart check",
            patient_id=patients[2].id,
            doctor_id=doctors[0].id
        ),
        Appointment(
            date=date(2025, 11, 24),
            time=time(16, 0),
            notes="Dermatology follow-up",
            patient_id=patients[1].id,
            doctor_id=doctors[1].id
        ),
    ]
    db.session.add_all(appointments)
    db.session.commit()

    print("✅ Database seeded successfully! 🎉")
