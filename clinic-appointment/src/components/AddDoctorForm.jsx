// src/components/AddDoctorForm.jsx
import { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function AddDoctorForm() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    specialty: "",
    phone: "",
  });

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.post("doctors/", formData);
      navigate("/doctors");
    } catch (err) {
      console.error("Error adding doctor:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
      <input name="specialty" placeholder="Specialty" value={formData.specialty} onChange={handleChange} required />
      <input name="phone" placeholder="Phone" value={formData.phone} onChange={handleChange} required />
      <button type="submit">Add Doctor</button>
    </form>
  );
}
