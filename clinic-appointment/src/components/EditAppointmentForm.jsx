// clinic-appointment/src/components/EditAppointmentForm.jsx
import { useState, useEffect } from "react";
import { fetchJSON } from "../api/client.jsx";
import { useNavigate, useParams } from "react-router-dom";

export default function EditAppointmentForm() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    date: "",
    time: "",
    notes: "",
    patient_id: "",
    doctor_id: "",
  });

  const [patients, setPatients] = useState([]);
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      try {
        // Load appointment
        const appointment = await fetchJSON(`/appointments/${id}`);
        setFormData(appointment);

        // Load patients + doctors
        const p = await fetchJSON("/patients/");
        const d = await fetchJSON("/doctors/");

        setPatients(p);
        setDoctors(d);
      } catch (err) {
        console.error("Error loading appointment:", err);
      }
    };
    loadData();
  }, [id]);

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetchJSON(`/appointments/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      navigate("/appointments");
    } catch (err) {
      console.error("Error updating appointment:", err);
    }
  };

  return (
    <div className="container">
      <h2>Edit Appointment</h2>
      <form onSubmit={handleSubmit}>
        <input type="date" name="date" value={formData.date} onChange={handleChange} required />
        <input type="time" name="time" value={formData.time} onChange={handleChange} required />
        <input type="text" name="notes" value={formData.notes} onChange={handleChange} placeholder="Notes" required />

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

        <button type="submit">Save</button>
      </form>
    </div>
  );
}
