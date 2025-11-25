import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate, useParams } from "react-router-dom";

export default function EditDoctorForm() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({ name: "", specialty: "", phone: "" });

  useEffect(() => {
    const fetchDoctor = async () => {
      try {
        const data = await API.get(`doctors/${id}/`);
        setFormData(data);
      } catch (err) {
        console.error("Error fetching doctor:", err);
      }
    };
    fetchDoctor();
  }, [id]);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.put(`doctors/${id}/`, formData);
      navigate("/doctors");
    } catch (err) {
      console.error("Error updating doctor:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
      <input name="specialty" placeholder="Specialty" value={formData.specialty} onChange={handleChange} required />
      <input name="phone" placeholder="Phone" value={formData.phone} onChange={handleChange} required />
      <button type="submit">Save</button>
    </form>
  );
}
