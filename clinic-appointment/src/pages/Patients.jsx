// src/pages/Patients.jsx
import { useEffect, useState } from "react";
import PatientsForm from "../components/PatientsForm.jsx";
import { fetchJSON } from "../api/client";

export default function PatientsPage() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    fetchJSON("/patients")
      .then(data => setPatients(data))
      .catch(err => console.error("Failed to fetch patients", err));
  }, []);

  const handleNewPatient = (patient) => setPatients(prev => [...prev, patient]);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Patients</h1>
      <PatientsForm onCreated={handleNewPatient} />
      <ul className="mt-4">
        {patients.map(p => (
          <li key={p.id} className="border p-2 rounded mb-2">
            {p.name}, Age: {p.age}, Gender: {p.gender}, Phone: {p.phone}
          </li>
        ))}
      </ul>
    </div>
  );
}