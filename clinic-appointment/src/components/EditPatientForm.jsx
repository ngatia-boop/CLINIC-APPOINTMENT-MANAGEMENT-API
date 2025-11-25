// clinic-appointment/src/components/EditPatientForm.jsx
import { useState, useEffect } from "react";
import { fetchJSON } from "../api/client.jsx";
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
        const data = await fetchJSON(`/patients/${id}`);
        const patient = data.patient || data;

        setFormData({
          name: patient.name || "",
          age: patient.age != null ? String(patient.age) : "",
          gender: patient.gender || "",
          phone: patient.phone || "",
        });
      } catch (err) {
        console.error("Error fetching patient:", err);
      }
    };
    fetchPatient();
  }, [id]);

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetchJSON(`/patients/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...formData, age: Number(formData.age) }),
      });
      navigate("/patients");
    } catch (err) {
      console.error("Error updating patient:", err);
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "auto" }}>
      <h2>Edit Patient</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input name="name" value={formData.name} onChange={handleChange} required />

        <label>Age:</label>
        <input name="age" type="number" value={formData.age} onChange={handleChange} required />

        <label>Gender:</label>
        <select name="gender" value={formData.gender} onChange={handleChange} required>
          <option value="">Select gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>

        <label>Phone:</label>
        <input name="phone" type="tel" value={formData.phone} onChange={handleChange} required />

        <button type="submit" style={{ marginTop: "10px" }}>Save</button>
      </form>
    </div>
  );
}
