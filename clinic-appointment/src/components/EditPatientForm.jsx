import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate, useParams } from "react-router-dom";

export default function EditPatientForm() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    age: "",
    gender: "",
    phone: "",
  });

  useEffect(() => {
    const fetchPatient = async () => {
      try {
        const data = await API.get(`patients/${id}/`);
        setFormData({
          name: data.name || "",
          age: data.age != null ? String(data.age) : "",
          gender: data.gender || "",
          phone: data.phone || "",
        });
      } catch (err) {
        console.error("Error fetching patient:", err);
      }
    };
    fetchPatient();
  }, [id]);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.put(`patients/${id}/`, { ...formData, age: Number(formData.age) });
      navigate("/patients");
    } catch (err) {
      console.error("Error updating patient:", err);
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
      <button type="submit">Save</button>
    </form>
  );
}
