from datetime import datetime
from extensions import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.String(255), nullable=False)

    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)

    # Relationships
    patient = db.relationship('Patient', back_populates='appointments')
    doctor = db.relationship('Doctor', back_populates='appointments')

    def to_dict(self, include_patient=False, include_doctor=False):
        data = {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d"),
            "time": self.time.strftime("%H:%M"),
            "notes": self.notes,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
        }

        if include_patient and self.patient:
            data["patient"] = self.patient.to_dict()

        if include_doctor and self.doctor:
            data["doctor"] = self.doctor.to_dict()

        return data
