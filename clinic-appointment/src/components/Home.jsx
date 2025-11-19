import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center", // vertical centering
        alignItems: "center",     // horizontal centering
        height: "80vh",           // take most of the viewport height
        textAlign: "center",      // center text
        padding: "20px",
        background: "#f0f8ff",    // light background
      }}
    >
      <h1>🏥 Welcome to Clinic Management System</h1>
      <p>Manage your patients, doctors, and appointments easily! ✨📊</p>
      <img
        src="https://plus.unsplash.com/premium_photo-1682130157004-057c137d96d5?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2xpbmljfGVufDB8fDB8fHww"
        alt="clinic"
        style={{ marginTop: "20px", borderRadius: "10px", width: "300px" }}
      />
    </div>
  );
}

