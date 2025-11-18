import { useState } from "react";
import { fetchJSON } from "../api/client";

export default function PatientsForm({ onCreated }) {
  const [form, setForm] = useState({
    name: "",
    age: "",
    gender: "",
    phone: "",
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    const newPatient = await fetchJSON("/patients", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    if (onCreated) onCreated(newPatient);

    setForm({ name: "", age: "", gender: "", phone: "" });
  }

  return (
    <form onSubmit={handleSubmit} className="p-4 grid gap-3 bg-white rounded-xl shadow">
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Name"
        className="p-2 rounded border"
      />
      <input
        name="age"
        value={form.age}
        onChange={handleChange}
        placeholder="Age"
        className="p-2 rounded border"
      />
      <input
        name="gender"
        value={form.gender}
        onChange={handleChange}
        placeholder="Gender"
        className="p-2 rounded border"
      />
      <input
        name="phone"
        value={form.phone}
        onChange={handleChange}
        placeholder="Phone"
        className="p-2 rounded border"
      />
      <button className="p-2 bg-green-600 text-white rounded-xl hover:bg-green-700 transition">
        Add Patient
      </button>
    </form>
  );
}

