import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function AddAppointmentForm() {
  const [formData, setFormData] = useState({ date: "", time: "", notes: "", patient_id: "", doctor_id: "" });
  const [patients, setPatients] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const p = await API.get("/patients/");
      const d = await API.get("/doctors/");
      setPatients(p.data);
      setDoctors(d.data);
    };
    fetchData();
  }, []);

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    await API.post("/appointments/", formData);
    navigate("/appointments");
  };

  return (
    <div className="container">
      <h2>Add Appointment</h2>
      <form onSubmit={handleSubmit}>
        <input type="date" name="date" value={formData.date} onChange={handleChange} required />
        <input type="time" name="time" value={formData.time} onChange={handleChange} required />
        <input type="text" name="notes" value={formData.notes} onChange={handleChange} placeholder="Notes" required />
        
        <select name="patient_id" value={formData.patient_id} onChange={handleChange} required>
          <option value="">Select Patient</option>
          {patients.map(p => (
            <option key={p.id} value={p.id}>{p.name}</option>
          ))}
        </select>

        <select name="doctor_id" value={formData.doctor_id} onChange={handleChange}>
          <option value="">Select Doctor</option>
          {doctors.map(d => (
            <option key={d.id} value={d.id}>{d.name}</option>
          ))}
        </select>

        <button type="submit">Save</button>
      </form>
    </div>
  );
}
