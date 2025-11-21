# backend/main.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.extensions import db
from backend.models import Patient, Doctor, Appointment
from datetime import date, time

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["*"])  # Allow all origins for now
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'  # or your preferred DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        # Create tables
        db.create_all()

        # --- SEED DATA ---
        if not Patient.query.first():  # Only seed if database is empty
            print("🌱 Seeding database...")

            doctors = [
                Doctor(name="Dr. Sarah Kim", specialization="Cardiology", phone="0712345678"),
                Doctor(name="Dr. John Mwangi", specialization="Dermatology", phone="0798765432"),
                Doctor(name="Dr. Diana Kithinji", specialization="Psychologist", phone="0700987654"),
            ]
            db.session.add_all(doctors)
            db.session.commit()  # Commit first to generate IDs

            patients = [
                Patient(name="Alice Wanjiku", age=28, gender="Female", phone="0700001111"),
                Patient(name="Brian Otieno", age=34, gender="Male", phone="0700002222"),
                Patient(name="Charles Mwangi", age=45, gender="Male", phone="0700003333"),
                Patient(name="Diana Njeri", age=32, gender="Female", phone="0700004444"),
            ]
            db.session.add_all(patients)
            db.session.commit()  # Commit to generate IDs

            appointments = [
                Appointment(date=date(2025, 11, 20), time=time(10, 30),
                            notes="Routine checkup", patient_id=patients[0].id, doctor_id=doctors[0].id),
                Appointment(date=date(2025, 11, 21), time=time(14, 15),
                            notes="Skin rash treatment", patient_id=patients[1].id, doctor_id=doctors[1].id),
                Appointment(date=date(2025, 11, 22), time=time(9, 0),
                            notes="Psychology consultation", patient_id=patients[3].id, doctor_id=doctors[2].id),
                Appointment(date=date(2025, 11, 23), time=time(11, 45),
                            notes="Follow-up heart check", patient_id=patients[2].id, doctor_id=doctors[0].id),
                Appointment(date=date(2025, 11, 24), time=time(16, 0),
                            notes="Dermatology follow-up", patient_id=patients[1].id, doctor_id=doctors[1].id),
            ]
            db.session.add_all(appointments)
            db.session.commit()
            print("✅ Database seeded successfully!")

    # ----------------- ROUTES ----------------- #
    @app.route("/patients", methods=["GET"])
    def get_patients():
        patients = Patient.query.all()
        return jsonify([{
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "phone": p.phone
        } for p in patients])

    @app.route("/doctors", methods=["GET"])
    def get_doctors():
        doctors = Doctor.query.all()
        return jsonify([{
            "id": d.id,
            "name": d.name,
            "specialization": d.specialization,
            "phone": d.phone
        } for d in doctors])

    @app.route("/appointments", methods=["GET"])
    def get_appointments():
        appointments = Appointment.query.all()
        return jsonify([{
            "id": a.id,
            "date": a.date.isoformat(),
            "time": a.time.isoformat(),
            "notes": a.notes,
            "patient_id": a.patient_id,
            "doctor_id": a.doctor_id
        } for a in appointments])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5555, debug=True)
