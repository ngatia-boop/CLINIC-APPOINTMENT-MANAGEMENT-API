import { useEffect, useState } from "react";
import { fetchJSON } from "../api/client.jsx";
import { Link } from "react-router-dom";

export default function PatientList() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const loadPatients = async () => {
      try {
        const data = await fetchJSON("/patients/");
        setPatients(data);
      } catch (err) {
        console.error("Failed to fetch patients:", err);
      }
    };
    loadPatients();
  }, []);

  const deletePatient = async (id) => {
    if (!window.confirm("Are you sure you want to delete this patient?")) return;

    try {
      await fetchJSON(`/patients/${id}`, { method: "DELETE" });
      setPatients((prev) => prev.filter((p) => p.id !== id));
    } catch (err) {
      console.error("Failed to delete patient:", err);
    }
  };

  return (
    <div className="container">
      <h2>Patients</h2>
      <Link to="/patients/add">
        <button>Add Patient</button>
      </Link>
      <ul>
        {patients.map((p) => (
          <li key={p.id}>
            {p.name} | {p.age} years | {p.gender}
            <Link to={`/patients/edit/${p.id}`}>
              <button>Edit</button>
            </Link>
            <button onClick={() => deletePatient(p.id)}>🗑 Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
