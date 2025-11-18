// src/pages/Appointments.jsx
import { useEffect, useState } from "react";
import AppointmentForm from "../components/AppointmentForm.jsx"; 
import { fetchJSON } from "../api/client.jsx";

export default function AppointmentsPage() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    fetchJSON("/appointments")
      .then((data) => setAppointments(data))
      .catch((err) => console.error("Failed to fetch appointments", err));
  }, []);

  const handleNewAppointment = (appt) => {
    setAppointments((prev) => [...prev, appt]);
  };

  const handleDeleted = (id) => {
    setAppointments((prev) => prev.filter((a) => a.id !== id));
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Appointments</h1>
      <AppointmentForm onCreated={handleNewAppointment} />
      <ul className="mt-4 space-y-2">
        {appointments.map((a) => (
          <li key={a.id} className="border p-2 rounded">
            {a.patient?.name ?? "Unknown"} with {a.doctor?.name ?? "Unknown"} on {a.date} at {a.time}
            <button
              className="bg-red-500 text-white px-2 py-1 ml-2 rounded"
              onClick={async () => {
                await fetchJSON(`/appointments/${a.id}`, { method: "DELETE" });
                handleDeleted(a.id);
              }}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
