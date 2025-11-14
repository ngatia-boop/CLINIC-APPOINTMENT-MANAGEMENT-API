from clinic_backend.config import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)  # primary key is mandatory
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    # Foreign key linking to Patient
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'description': self.description,
            'patient_id': self.patient_id
        }
