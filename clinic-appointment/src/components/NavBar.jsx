// src/components/NavBar.jsx
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav style={styles.nav}>
      <h2 style={styles.title}>Clinic Appointment System</h2>
      <div style={styles.links}>
        <Link to="/" style={styles.link}>Home</Link>
        <Link to="/patients" style={styles.link}>Patients</Link>
        <Link to="/appointments" style={styles.link}>Appointments</Link>
        <Link to="/doctors" style={styles.link}>Doctors</Link>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    backgroundColor: "#007bff",
    padding: "10px 20px",
    color: "#fff",
  },
  title: { margin: 0 },
  links: { display: "flex", gap: "15px" },
  link: { color: "white", textDecoration: "none", fontWeight: "bold" },
};

export default NavBar;
