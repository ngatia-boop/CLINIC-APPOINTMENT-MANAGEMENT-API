// src/components/AppointmentForm.jsx
import { useState } from "react";

function AppointmentForm({ onSubmit, initialData = {} }) {
  const [formData, setFormData] = useState({
    patientName: initialData.patientName || "",
    doctorName: initialData.doctorName || "",
    date: initialData.date || "",
    time: initialData.time || "",
    reason: initialData.reason || "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (onSubmit) onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <h3>Schedule Appointment</h3>

      <label>Patient Name:</label>
      <input
        type="text"
        name="patientName"
        value={formData.patientName}
        onChange={handleChange}
        required
      />

      <label>Doctor Name:</label>
      <input
        type="text"
        name="doctorName"
        value={formData.doctorName}
        onChange={handleChange}
        required
      />

      <label>Date:</label>
      <input
        type="date"
        name="date"
        value={formData.date}
        onChange={handleChange}
        required
      />

      <label>Time:</label>
      <input
        type="time"
        name="time"
        value={formData.time}
        onChange={handleChange}
        required
      />

      <label>Reason:</label>
      <textarea
        name="reason"
        value={formData.reason}
        onChange={handleChange}
        rows="3"
      />

      <button type="submit">Save Appointment</button>
    </form>
  );
}

const styles = {
  form: {
    display: "flex",
    flexDirection: "column",
    maxWidth: "400px",
    gap: "10px",
    padding: "15px",
    border: "1px solid #ccc",
    borderRadius: "8px",
  },
};

export default AppointmentForm;
