import { useEffect, useState } from 'react'
import DoctorCard from '../components/DoctorCard'

function Doctors() {
  const [doctors, setDoctors] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/doctors/')
      .then((res) => res.json())
      .then(setDoctors)
      .catch((err) => console.error('Error fetching doctors:', err))
  }, [])

  return (
    <div>
      <h2>Doctors</h2>
      {doctors.length === 0 ? (
        <p>No doctors available at the moment.</p>
      ) : (
        <ul>
          {doctors.map((doctor) => (
            <li key={doctor.id}>
              <strong>Dr. {doctor.name}</strong> — {doctor.specialty}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default Doctors
