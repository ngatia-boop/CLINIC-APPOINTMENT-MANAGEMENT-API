import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home.jsx";
import Patients from "./pages/Patients.jsx";
import Appointments from "./pages/Appointments.jsx";
import Doctors from "./pages/Doctors.jsx";
import "./styles/app.css";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link>{" | "}
        <Link to="/patients">Patients</Link>{" | "}
        <Link to="/appointments">Appointments</Link>{" | "}
        <Link to="/doctors">Doctors</Link>
      </nav>

      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/patients" element={<Patients />} />
          <Route path="/appointments" element={<Appointments />} />
          <Route path="/doctors" element={<Doctors />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
