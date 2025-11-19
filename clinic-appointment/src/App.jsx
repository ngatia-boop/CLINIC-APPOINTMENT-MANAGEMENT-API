import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import PatientList from "./components/PatientList";
import AddPatientForm from "./components/AddPatientForm";
import EditPatientForm from "./components/EditPatientForm";

import DoctorList from "./components/DoctorList";
import AddDoctorForm from "./components/AddDoctorForm";
import EditDoctorForm from "./components/EditDoctorForm";

import AppointmentList from "./components/AppointmentList";
import AddAppointmentForm from "./components/AddAppointmentForm";
import EditAppointmentForm from "./components/EditAppointmentForm";

import "./styles/app.css";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        
        {/* Patients */}
        <Route path="/patients" element={<PatientList />} />
        <Route path="/patients/add" element={<AddPatientForm />} />
        <Route path="/patients/edit/:id" element={<EditPatientForm />} />
       
        {/* Doctors */}
        <Route path="/doctors" element={<DoctorList />} />
        <Route path="/doctors/add" element={<AddDoctorForm />} />
        <Route path="/doctors/edit/:id" element={<EditDoctorForm />} />

        {/* Appointments */}
        <Route path="/appointments" element={<AppointmentList />} />
        <Route path="/appointments/add" element={<AddAppointmentForm />} />
        <Route path="/appointments/edit/:id" element={<EditAppointmentForm />} />

        {/* Default / fallback */}
        <Route path="/" element={<PatientList />} />
      </Routes>
    </Router>
  );
}

export default App;
