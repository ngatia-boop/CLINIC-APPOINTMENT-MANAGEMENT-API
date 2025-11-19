import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate, useParams } from "react-router-dom";

export default function EditDoctorForm() {
  const { id } = useParams();
  const [formData, setFormData] = useState({ name: "", specialty: "", phone: "" });
  const navigate = useNavigate();

  useEffect(() => {
    const fetchDoctor = async () => {
      const res = await API.get(`/doctors/${id}`);
      setFormData(res.data);
    };
    fetchDoctor();
  }, [id]);

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    await API.put(`/doctors/${id}`, formData);
    navigate("/doctors");
  };

  return (
    <div className="container">
      <h2>Edit Doctor</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
        <input name="specialty" value={formData.specialty} onChange={handleChange} placeholder="Specialty" required />
        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}
