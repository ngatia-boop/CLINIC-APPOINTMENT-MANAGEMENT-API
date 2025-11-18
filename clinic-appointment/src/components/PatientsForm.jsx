// src/components/PatientsForm.jsx
import { useState } from "react";
import { fetchJSON } from "../api/client.jsx";

export default function PatientsForm({ onCreated }) {
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    gender: "",
    phone: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newPatient = await fetchJSON("/patients", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      onCreated(newPatient); // update parent list
      setFormData({ name: "", age: "", gender: "", phone: "" });
    } catch (err) {
      console.error("Failed to create patient:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="border p-4 rounded space-y-2">
      <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
      <input name="age" type="number" value={formData.age} onChange={handleChange} placeholder="Age" required />
      <select name="gender" value={formData.gender} onChange={handleChange} required>
        <option value="">Select Gender</option>
        <option value="Female">Female</option>
        <option value="Male">Male</option>
      </select>
      <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />

      <button type="submit" className="bg-green-500 text-white px-2 py-1 rounded">Add Patient</button>
    </form>
  );
}
