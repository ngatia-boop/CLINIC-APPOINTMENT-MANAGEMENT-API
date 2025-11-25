// clinic-appointment/src/components/EditDoctorForm.jsx
import { useState, useEffect } from "react";
import { fetchJSON } from "../api/client.jsx";
import { useNavigate, useParams } from "react-router-dom";

export default function EditDoctorForm() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    specialty: "",
    phone: "",
  });

  useEffect(() => {
    const fetchDoctor = async () => {
      try {
        const data = await fetchJSON(`/doctors/${id}`);
        setFormData(data);
      } catch (err) {
        console.error("Failed to fetch doctor:", err);
      }
    };
    fetchDoctor();
  }, [id]);

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetchJSON(`/doctors/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      navigate("/doctors");
    } catch (err) {
      console.error("Failed to update doctor:", err);
    }
  };

  return (
    <div className="container">
      <h2>Edit Doctor</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} required />
        <input name="specialty" value={formData.specialty} onChange={handleChange} required />
        <input name="phone" value={formData.phone} onChange={handleChange} required />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}
