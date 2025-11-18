import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function DoctorList() {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const fetchDoctors = async () => {
      try{
      const res = await API.get("http://127.0.0.1:5555/doctors/");
      setDoctors(res.data);
    } catch (err){
      console.error("Failed to fetch doctors:", err);
    }
  };
    fetchDoctors();
  }, []);

  return (
    <div className="container">
      <h2>Doctors</h2>
      <Link to="/doctors/add">
        <button>Add Doctor</button>
      </Link>
      <ul>
        {doctors.map(d => (
          <li key={d.id}>
            {d.name} - {d.specialty} - {d.phone}
            <Link to={`/doctors/edit/${d.id}`}><button>Edit</button></Link>
          </li>
        ))}
      </ul>
    </div>
  );
}