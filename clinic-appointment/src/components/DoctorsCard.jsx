// src/components/DoctorsCard.jsx
import { useState } from "react";
import { fetchJSON } from "../api/client.jsx";

export default function DoctorsCard({ doctor, onUpdated, onDeleted }) {
  const [editing, setEditing] = useState(false);
  const [name, setName] = useState(doctor.name);
  const [specialization, setSpecialization] = useState(doctor.specialization);
  const [phone, setPhone] = useState(doctor.phone);

  const handleUpdate = async () => {
    try {
      const updatedDoctor = await fetchJSON(`/doctors/${doctor.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, specialization, phone }),
      });
      onUpdated(updatedDoctor);
      setEditing(false);
    } catch (err) {
      console.error("Failed to update doctor:", err);
    }
  };

  const handleDelete = async () => {
    if (!confirm("Delete this doctor?")) return;
    try {
      await fetchJSON(`/doctors/${doctor.id}`, { method: "DELETE" });
      onDeleted(doctor.id);
    } catch (err) {
      console.error("Failed to delete doctor:", err);
    }
  };

  return (
    <div className="border p-4 rounded space-y-2">
      {editing ? (
        <>
          <input value={name} onChange={(e) => setName(e.target.value)} />
          <input value={specialization} onChange={(e) => setSpecialization(e.target.value)} />
          <input value={phone} onChange={(e) => setPhone(e.target.value)} />
          <button onClick={handleUpdate} className="bg-blue-500 text-white px-2 py-1 rounded">Save</button>
          <button onClick={() => setEditing(false)} className="bg-gray-300 px-2 py-1 rounded">Cancel</button>
        </>
      ) : (
        <>
          <h3 className="font-bold">{doctor.name}</h3>
          <p>{doctor.specialization}</p>
          <p>{doctor.phone}</p>
          <button onClick={() => setEditing(true)} className="bg-yellow-500 px-2 py-1 rounded">Edit</button>
          <button onClick={handleDelete} className="bg-red-500 text-white px-2 py-1 rounded">Delete</button>
        </>
      )}
    </div>
  );
}
