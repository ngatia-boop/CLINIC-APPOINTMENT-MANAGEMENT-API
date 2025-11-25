// clinic-appointment/src/components/DoctorList.jsx
import { useEffect, useState } from "react";
import { fetchJSON } from "../api/client.jsx";
import { Link } from "react-router-dom";

export default function DoctorList() {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const loadDoctors = async () => {
      try {
        const data = await fetchJSON("/doctors/");
        setDoctors(data);
      } catch (err) {
        console.error("Failed to fetch doctors:", err);
      }
    };
    loadDoctors();
  }, []);

  const deleteDoctor = async (id) => {
    if (!window.confirm("Are you sure you want to delete this doctor?")) return;

    try {
      await fetchJSON(`/doctors/${id}`, { method: "DELETE" });
      setDoctors((prev) => prev.filter((d) => d.id !== id));
    } catch (err) {
      console.error("Failed to delete doctor:", err);
    }
  };

  return (
    <div className="container">
      <h2>Doctors</h2>
      <Link to="/doctors/add">
        <button>Add Doctor</button>
      </Link>

      <ul>
        {doctors.map((d) => (
          <li key={d.id}>
            {d.name} | {d.specialty}{" "}
            <Link to={`/doctors/edit/${d.id}`}>
              <button>Edit</button>
            </Link>{" "}
            <button onClick={() => deleteDoctor(d.id)}>🗑 Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
