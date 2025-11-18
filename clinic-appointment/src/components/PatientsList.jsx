import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function PatientList() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const fetchPatients = async () => {
      try{
      const res = await API.get("/patients/");
      setPatients(res.data);
    } catch (err) {
      console.error("Failed to fetch patients:",err);
    }
    };
    fetchPatients();
  }, []);

  return (
    <div className="container">
      <h2>Patients</h2>
      <Link to="/patients/add">
        <button>Add Patient</button>
      </Link>
      <ul>
        {patients.map(p => (
          <li key={p.id}>
            {p.name} ({p.age} years) - {p.gender} - {p.phone}
            <Link to={`/patients/edit/${p.id}`}><button>Edit</button></Link>
          </li>
        ))}
      </ul>
    </div>
  );
}