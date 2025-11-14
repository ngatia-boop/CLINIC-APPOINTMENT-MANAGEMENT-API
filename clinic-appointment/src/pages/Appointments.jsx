import { useState, useEffect } from "react"

function Appointments() {
  const [appointments, setAppointments] = useState([])

  useEffect(() => {
    // Fetch data from backend API
    fetch("/api/appointments")
      .then((r) => r.json())
      .then(setAppointments)
  }, [])

  return (
    <div className="appointments-page">
      <h2>All Appointments</h2>
      <ul>
        {appointments.map((appt) => (
          <li key={appt.id}>
            {appt.patient_name} — {appt.date}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default Appointments
