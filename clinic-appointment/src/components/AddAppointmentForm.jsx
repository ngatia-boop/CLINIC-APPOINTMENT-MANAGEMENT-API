// src/components/AddAppointmentForm.jsx
import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function AddAppointmentForm() {
  const navigate = useNavigate();
  const [patients, setPatients] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [formData, setFormData] = useState({
    patient_id: "",
    doctor_id: "",
    date: "",
    time: "",
    notes: "",
  });

  useEffect(() => {
    const fetchData = async () => {
      const p = await API.get("patients/");
      const d = await API.get("doctors/");
      setPatients(p);
      setDoctors(d);
    };
    fetchData();
  }, []);

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.post("appointments/", formData);
      navigate("/appointments");
    } catch (err) {
      console.error("Error adding appointment:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <select name="patient_id" value={formData.patient_id} onChange={handleChange} required>
        <option value="">Select Patient</option>
        {patients.map((p) => (
          <option key={p.id} value={p.id}>{p.name}</option>
        ))}
      </select>

      <select name="doctor_id" value={formData.doctor_id} onChange={handleChange}>
        <option value="">Select Doctor</option>
        {doctors.map((d) => (
          <option key={d.id} value={d.id}>{d.name}</option>
        ))}
      </select>

      <input type="date" name="date" value={formData.date} onChange={handleChange} required />
      <input type="time" name="time" value={formData.time} onChange={handleChange} required />
      <input type="text" name="notes" placeholder="Notes" value={formData.notes} onChange={handleChange} />

      <button type="submit">Add Appointment</button>
    </form>
  );
}
