import { useState, useEffect } from "react";
import API from "../api";
import { useNavigate, useParams } from "react-router-dom";

export default function EditPatientForm() {
  const { id } = useParams();
  const navigate = useNavigate();

  // Initialize all fields as empty strings
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    gender: "",
    phone: "",
  });

  // Fetch patient details once
  useEffect(() => {
    const fetchPatient = async () => {
      try {
        const res = await API.get(`/patients/${id}`);
        // Handle both { patient: {...} } and {...} response shapes
        const data = res.data.patient || res.data;

        setFormData({
          name: data.name || "",
          age: data.age != null ? String(data.age) : "", // safe string conversion
          gender: data.gender || "",
          phone: data.phone || "",
        });
      } catch (err) {
        console.error("Error fetching patient:", err);
        // Optional: show an error message or redirect
      }
    };
    fetchPatient();
  }, [id, navigate]); // include navigate if ESLint warns

  // Handle input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Submit updated data
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.put(`/patients/${id}`, {
        ...formData,
        age: Number(formData.age), // backend expects number
      });
      navigate("/patients");
    } catch (err) {
      console.error("Error updating patient:", err);
      // Optional: show error feedback to user
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "auto" }}>
      <h2>Edit Patient</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          name="name"
          type="text"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <label>Age:</label>
        <input
          name="age"
          type="number"
          value={formData.age}
          onChange={handleChange}
          required
        />

        <label>Gender:</label>
        {/* Consider using a select for consistency */}
        <select
          name="gender"
          value={formData.gender}
          onChange={handleChange}
          required
        >
          <option value="">Select gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>

        <label>Phone:</label>
        <input
          name="phone"
          type="tel"
          value={formData.phone}
          onChange={handleChange}
          required
        />

        <button type="submit" style={{ marginTop: "10px" }}>
          Save
        </button>
      </form>
    </div>
  );
}