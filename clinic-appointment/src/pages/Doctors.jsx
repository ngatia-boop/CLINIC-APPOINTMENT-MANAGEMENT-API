// src/pages/Doctors.jsx
import { useEffect, useState } from "react";
import DoctorsCard from "../components/DoctorsCard.jsx";
import { fetchJSON } from "../api/client.jsx";

export default function DoctorsPage() {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    fetchJSON("/doctors")
      .then((data) => setDoctors(data))
      .catch((err) => console.error("Failed to fetch doctors", err));
  }, []);

  const handleUpdated = (updatedDoctor) => {
    setDoctors((prev) =>
      prev.map((d) => (d.id === updatedDoctor.id ? updatedDoctor : d))
    );
  };

  const handleDeleted = (id) => {
    setDoctors((prev) => prev.filter((d) => d.id !== id));
  };

  return (
    <div className="p-4 grid gap-4">
      <h1 className="text-2xl font-bold mb-4">Doctors</h1>
      {doctors.map((d) => (
        <DoctorsCard
          key={d.id}
          doctor={d}
          onUpdated={handleUpdated}
          onDeleted={handleDeleted}
        />
      ))}
    </div>
  );
}
