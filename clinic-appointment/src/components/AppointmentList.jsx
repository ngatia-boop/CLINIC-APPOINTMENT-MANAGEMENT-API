// clinic-appointment/src/components/AppointmentList.jsx
import { useEffect, useState } from "react";
import { fetchJSON } from "../api/client.jsx";
import { Link } from "react-router-dom";

export default function AppointmentList() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const loadAppointments = async () => {
      try {
        const data = await fetchJSON("/appointments/");
        setAppointments(data);
      } catch (err) {
        console.error("Failed to fetch appointments:", err);
      }
    };
    loadAppointments();
  }, []);

  const deleteAppointment = async (id) => {
    if (!window.confirm("Are you sure you want to delete this appointment?")) return;

    try {
      await fetchJSON(`/appointments/${id}`, { method: "DELETE" });
      setAppointments((prev) => prev.filter((a) => a.id !== id));
    } catch (err) {
      console.error("Failed to delete appointment:", err);
    }
  };

  return (
    <div className="container">
      <h2>Appointments</h2>
      <Link to="/appointments/add">
        <button>Add Appointment</button>
      </Link>

      <ul>
        {appointments.map((a) => (
          <li key={a.id}>
            {a.patient?.name} → {a.doctor?.name || "No doctor"} | {a.date} {a.time}{" "}
            <Link to={`/appointments/edit/${a.id}`}>
              <button>Edit</button>
            </Link>{" "}
            <button onClick={() => deleteAppointment(a.id)}>🗑 Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
