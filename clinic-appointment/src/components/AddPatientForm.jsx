// src/components/AddPatientForm.jsx
import { useState } from "react";
import API from "../api";
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
      await API.post("patients/", { 
        ...formData,
        age: Number(formData.age) // ensure number
      });
      navigate("/patients");
    } catch (err) {
      console.error("Error adding patient:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
      <input name="age" type="number" placeholder="Age" value={formData.age} onChange={handleChange} required />
      <select name="gender" value={formData.gender} onChange={handleChange} required>
        <option value="">Select Gender</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>
      <input name="phone" placeholder="Phone" value={formData.phone} onChange={handleChange} required />
      <button type="submit">Add Patient</button>
    </form>
  );
}

