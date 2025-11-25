import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function AppointmentList() {
  const [appointments, setAppointments] = useState([]);
  const [patients, setPatients] = useState([]);
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
  const fetchData = async () => {
    try {
      const appts = await API.get("appointments/");
      const pats = await API.get("patients/");
      const docs = await API.get("doctors/");

      setAppointments(appts.data);
      setPatients(pats.data);
      setDoctors(docs.data);
    } catch (err) {
      console.error("Failed to fetch appointments:", err);
    }
  };
  fetchData();
}, []);


  const deleteAppointment = async (id) => {
    if (window.confirm("Are you sure you want to delete this appointment?")) {
      try {
        await API.delete(`appointments/${id}/`);
        setAppointments(appointments.filter((a) => a.id !== id));
      } catch (err) {
        console.error("Failed to delete appointment:", err);
      }
    }
  };

  const getPatientName = (id) => patients.find((p) => p.id === id)?.name || "Unknown";
  const getDoctorName = (id) => doctors.find((d) => d.id === id)?.name || "Unknown";

  return (
    <div>
      <h2>Appointments</h2>
      <Link to="/appointments/add"><button>Add Appointment</button></Link>
      <ul>
        {appointments.map((a) => (
          <li key={a.id}>
            {getPatientName(a.patient_id)} → {getDoctorName(a.doctor_id)} |
            {a.date} {a.time}
            <Link to={`/appointments/edit/${a.id}`}><button>Edit</button></Link>
            <button onClick={() => deleteAppointment(a.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

