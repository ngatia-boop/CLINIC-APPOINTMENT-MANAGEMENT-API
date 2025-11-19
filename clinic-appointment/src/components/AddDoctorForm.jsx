import { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function AddDoctorForm() {
  const [formData, setFormData] = useState({ name: "", specialization: "", phone: "" });
  const navigate = useNavigate();

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    await API.post("/doctors/", formData);
    navigate("/doctors");
  };

  return (
    <div className="container">
      <h2>Add Doctor</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
        <input name="specialization" value={formData.specialty} onChange={handleChange} placeholder="Specialty" required />
        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}
