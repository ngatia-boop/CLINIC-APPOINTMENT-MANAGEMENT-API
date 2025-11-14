// src/components/PatientForm.jsx
import { useState } from "react";

function PatientForm({ onSubmit, initialData = {} }) {
  const [formData, setFormData] = useState({
    name: initialData.name || "",
    age: initialData.age || "",
    gender: initialData.gender || "",
    contact: initialData.contact || "",
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
      <h3>Add / Edit Patient</h3>

      <label>Name:</label>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleChange}
        required
      />

      <label>Age:</label>
      <input
        type="number"
        name="age"
        value={formData.age}
        onChange={handleChange}
        required
      />

      <label>Gender:</label>
      <select
        name="gender"
        value={formData.gender}
        onChange={handleChange}
        required
      >
        <option value="">Select gender</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>

      <label>Contact:</label>
      <input
        type="text"
        name="contact"
        value={formData.contact}
        onChange={handleChange}
        required
      />

      <button type="submit">Save Patient</button>
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

export default PatientForm;
