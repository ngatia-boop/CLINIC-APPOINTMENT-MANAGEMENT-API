import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function AppointmentList() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const fetchAppointments = async () => {
      try {
      const res = await API.get("http://127.0.0.1:5555/appointments/");
      setAppointments(res.data);
    } catch (err){
      console.error("Failed to fetch appointments:", err);
    }
  };
    fetchAppointments();
  }, []);

  return (
    <div className="container">
      <h2>Appointments</h2>
      <Link to="/appointments/add">
        <button>Add Appointment</button>
      </Link>
      <ul>
        {appointments.map(a => (
          <li key={a.id}>
            {a.patient?.name} → {a.doctor?.name || "No doctor"} | {a.date} {a.time}
            <Link to={`/appointments/edit/${a.id}`}><button>Edit</button></Link>
          </li>
        ))}
      </ul>
    </div>
  );
}