// src/pages/Doctors.jsx
import { useEffect, useState } from "react";
import DoctorsCard from "../components/DoctorsCard.jsx";
import { fetchJSON } from "../api/client";

export default function DoctorsPage() {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    fetchJSON("/doctors")
      .then(data => setDoctors(data))
      .catch(err => console.error("Failed to fetch doctors", err));
  }, []);

  const handleDelete = async (id) => {
    await fetchJSON(`/doctors/${id}`, { method: "DELETE" });
    setDoctors(prev => prev.filter(d => d.id !== id));
  };

  const handleUpdate = async (doctor) => {
    const updatedName = prompt("Enter new name", doctor.name);
    if (!updatedName) return;

    const updated = await fetchJSON(`/doctors/${doctor.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...doctor, name: updatedName }),
    });

    setDoctors(prev => prev.map(d => d.id === updated.id ? updated : d));
  };

  return (
    <div className="p-4 grid gap-4">
      <h1 className="text-2xl font-bold mb-4">Doctors</h1>
      {doctors.map(d => (
        <DoctorsCard key={d.id} doctor={d} onDelete={handleDelete} onUpdate={handleUpdate} />
      ))}
    </div>
  );
}