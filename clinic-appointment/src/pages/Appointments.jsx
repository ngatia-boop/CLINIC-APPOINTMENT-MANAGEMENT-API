// src/pages/Appointments.jsx
import { useEffect, useState } from "react";
import AppointmentForm from "../components/AppointmentsForm.jsx";
import { fetchJSON } from "../api/client";

export default function AppointmentsPage() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    fetchJSON("/appointments")
      .then(data => setAppointments(data))
      .catch(err => console.error("Failed to fetch appointments", err));
  }, []);

  const handleNewAppointment = (appt) => {
    setAppointments(prev => [...prev, appt]);
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Appointments</h1>
      <AppointmentForm onCreated={handleNewAppointment} />
      <ul className="mt-4">
        {appointments.map(a => (
          <li key={a.id}>
            {a.patient?.name ?? "Unknown"} with {a.doctor?.name ?? "Unknown"} on {a.date} at {a.time}
          </li>
        ))}
      </ul>
    </div>
  );
}
