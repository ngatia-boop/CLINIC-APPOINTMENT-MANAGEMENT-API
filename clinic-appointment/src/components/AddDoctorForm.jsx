// clinic-appointment/src/components/AddDoctorForm.jsx
import { useState } from "react";
import { fetchJSON } from "../api/client.jsx";
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
      await fetchJSON("/doctors", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      navigate("/doctors");
    } catch (err) {
      console.error("Error adding doctor:", err);
    }
  };

  return (
    <div className="container">
      <h2>Add Doctor</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />

        <input name="specialty" value={formData.specialty} onChange={handleChange} placeholder="Specialty" required />

        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />

        <button type="submit">Add Doctor</button>
      </form>
    </div>
  );
}
