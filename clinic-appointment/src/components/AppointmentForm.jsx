import { useState } from "react";
import { fetchJSON } from "../api/client";

export default function AppointmentForm({ onCreated }) {
  const [form, setForm] = useState({
    patient_id: "",
    doctor_id: "",
    date: "",
    time: "",
    notes: "",
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    const newAppointment = await fetchJSON("/appointments", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    if (onCreated) onCreated(newAppointment);

    setForm({ patient_id: "", doctor_id: "", date: "", time: "", notes: "" });
  }

  return (
    <form onSubmit={handleSubmit} className="p-4 grid gap-3 bg-white rounded-xl shadow">
      <input
        name="patient_id"
        value={form.patient_id}
        onChange={handleChange}
        placeholder="Patient ID"
        className="p-2 rounded border"
      />

      <input
        name="doctor_id"
        value={form.doctor_id}
        onChange={handleChange}
        placeholder="Doctor ID"
        className="p-2 rounded border"
      />

      <input
        type="date"
        name="date"
        value={form.date}
        onChange={handleChange}
        className="p-2 rounded border"
      />

      <input
        type="time"
        name="time"
        value={form.time}
        onChange={handleChange}
        className="p-2 rounded border"
      />

      <textarea
        name="notes"
        value={form.notes}
        onChange={handleChange}
        placeholder="Notes"
        className="p-2 rounded border"
      />

      <button className="p-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition">
        Create Appointment
      </button>
    </form>
  );
}

