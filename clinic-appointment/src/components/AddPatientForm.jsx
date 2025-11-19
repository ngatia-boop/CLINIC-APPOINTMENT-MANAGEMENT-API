import { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function AddPatientForm() {
  const [formData, setFormData] = useState({ name: "", age: "", gender: "", phone: "" });
  const navigate = useNavigate();

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    await API.post("/patients/", formData);
    navigate("/patients");
  };

  return (
    <div className="container">
      <h2>Add Patient</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
        <input name="age" type="number" value={formData.age} onChange={handleChange} placeholder="Age" required />
        <input name="gender" value={formData.gender} onChange={handleChange} placeholder="Gender" required />
        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}
