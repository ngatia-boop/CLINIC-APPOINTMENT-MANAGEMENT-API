from backend.extensions import db

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    # Relationship
    appointments = db.relationship('Appointment', back_populates='doctor', cascade="all, delete")

    def to_dict(self, include_appointments=False):
        data = {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "phone": self.phone,
        }

        if include_appointments:
            data["appointments"] = [
                appt.to_dict(include_patient=True) for appt in self.appointments
            ]

        return data
