from backend.extensions import db

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    # Relationship
    appointments = db.relationship('Appointment', back_populates='patient', cascade="all, delete")

    def to_dict(self, include_appointments=False):
        data = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "phone": self.phone,
        }

        if include_appointments:
            data["appointments"] = [appt.to_dict(include_doctor=True) for appt in self.appointments]

        return data
