import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import Home from "./pages/Home"
import Patients from "./pages/Patients"
import Appointments from "./pages/Appointments"
import "./styles/app.css"

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link>{" | "}
        <Link to="/patients">Patients</Link>{" | "}
        <Link to="/appointments">Appointments</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/patients" element={<Patients />} />
        <Route path="/appointments" element={<Appointments />} />
      </Routes>
    </Router>
  )
}

export default App
