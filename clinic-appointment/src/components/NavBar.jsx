import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 bg-blue-700 text-white shadow">
      <h1 className="text-xl font-bold">Clinic App</h1>
      <div className="flex gap-4">
        <Link to="/" className="hover:underline">Appointments</Link>
        <Link to="/patients" className="hover:underline">Patients</Link>
        <Link to="/doctors" className="hover:underline">Doctors</Link>
      </div>
    </nav>
  );
}