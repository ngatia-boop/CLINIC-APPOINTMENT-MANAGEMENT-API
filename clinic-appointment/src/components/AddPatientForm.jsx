// clinic-appointment/src/components/AddPatientForm.jsx
import { useState } from "react";
import { fetchJSON } from "../api/client.jsx";
import { useNavigate } from "react-router-dom";

export default function AddPatientForm() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    age: "",
    gender: "",
    phone: "",
  });

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetchJSON("/patients", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...formData, age: Number(formData.age) }),
      });
      navigate("/patients");
    } catch (err) {
      console.error("Error adding patient:", err);
    }
  };

  return (
    <div className="container">
      <h2>Add Patient</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />

        <input name="age" type="number" value={formData.age} onChange={handleChange} placeholder="Age" required />

        <select name="gender" value={formData.gender} onChange={handleChange} required>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />

        <button type="submit">Add Patient</button>
      </form>
    </div>
  );
}

