// src/components/AppointmentForm.jsx
import { useState, useEffect } from "react";
import { fetchJSON } from "../api/client.jsx";

export default function AppointmentForm({ onCreated }) {
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
    fetchJSON("/patients").then(setPatients).catch(console.error);
    fetchJSON("/doctors").then(setDoctors).catch(console.error);
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newAppt = await fetchJSON("/appointments", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      onCreated(newAppt); // update parent list
      setFormData({ patient_id: "", doctor_id: "", date: "", time: "", notes: "" });
    } catch (err) {
      console.error("Failed to create appointment:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="border p-4 rounded space-y-2">
      <select name="patient_id" value={formData.patient_id} onChange={handleChange} required>
        <option value="">Select patient</option>
        {patients.map((p) => (
          <option key={p.id} value={p.id}>{p.name}</option>
        ))}
      </select>

      <select name="doctor_id" value={formData.doctor_id} onChange={handleChange} required>
        <option value="">Select doctor</option>
        {doctors.map((d) => (
          <option key={d.id} value={d.id}>{d.name}</option>
        ))}
      </select>

      <input type="date" name="date" value={formData.date} onChange={handleChange} required />
      <input type="time" name="time" value={formData.time} onChange={handleChange} required />
      <input type="text" name="notes" value={formData.notes} onChange={handleChange} placeholder="Notes" />

      <button type="submit" className="bg-blue-500 text-white px-2 py-1 rounded">Add Appointment</button>
    </form>
  );
}
