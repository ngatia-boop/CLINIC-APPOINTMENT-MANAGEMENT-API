from backend import create_app
from backend.extensions import db
from backend.models import Patient, Doctor, Appointment
from datetime import date, time

app = create_app()

with app.app_context():

    print("🔥 Clearing old data...")
    Appointment.query.delete()
    Doctor.query.delete()
    Patient.query.delete()
    db.session.commit()

    print("🌱 Adding Doctors...")
    doc1 = Doctor(name="Dr. Sarah Kim", specialization="Cardiology", phone="0712345678")
    doc2 = Doctor(name="Dr. John Mwangi", specialization="Dermatology", phone="0798765432")
    doc3 = Doctor(name="DR. Diana Kithinji", specialization="Psychologist", phone="070098765")
    print("🌱 Adding Patients...")
    p1 = Patient(name="Alice Wanjiku", age=28, gender="Female", phone="0700001111")
    p2 = Patient(name="Brian Otieno", age=34, gender="Male", phone="0700002222")

    db.session.add_all([doc1, doc2,doc3, p1, p2])
    db.session.commit()

    print("🌱 Adding Appointments...")
    appt1 = Appointment(
        date=date(2025, 11, 20),
        time=time(10, 30),
        notes="Routine checkup",
        patient_id=p1.id,
        doctor_id=doc1.id
    )

    appt2 = Appointment(
        date=date(2025, 11, 21),
        time=time(14, 15),
        notes="Skin rash treatment",
        patient_id=p2.id,
        doctor_id=doc2.id
    )

    db.session.add_all([appt1, appt2])
    db.session.commit()

    print("✅ Database seeded successfully! 🎉")
