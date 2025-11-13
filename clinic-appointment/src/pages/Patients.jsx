import { useEffect, useState } from "react"

function Patients() {
  const [patients, setPatients] = useState([])

  useEffect(() => {
    fetch("/api/patients")
      .then((r) => r.json())
      .then(setPatients)
  }, [])

  return (
    <div className="patients-page">
      <h2>Patient List</h2>
      <ul>
        {patients.map((p) => (
          <li key={p.id}>{p.name} ({p.age} yrs)</li>
        ))}
      </ul>
    </div>
  )
}

export default Patients
