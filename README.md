🏥 Clinic Appointment Management App

A full-stack web application for managing patients, doctors, and appointments in a clinic.
Built with React (Vite) on the frontend and Flask on the backend.

📁 Project Structure
```
clinic-appointment-management-api/
├── server/                     # Flask backend
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   ├── config.py
│   └── ...
└── clinic-appointment/         # React frontend (Vite)
    ├── src/
    │   ├── pages/
    │   │   ├── Home.jsx
    │   │   ├── Patients.jsx
    │   │   ├── Appointments.jsx
    │   │   └── Doctors.jsx
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── index.css
    ├── vite.config.js
    ├── package.json
    └── ...
```

⚙️ Tech Stack
Layer	Technology
Frontend	React (Vite), React Router
Backend	Flask (Python)
Database	SQLite (via SQLAlchemy ORM)
API Communication	RESTful JSON
Dev Tools	npm, pipenv, Vite dev server, Flask CLI
🚀 Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/yourusername/clinic-appointment-management-api.git
cd clinic-appointment-management-api

2️⃣ Backend Setup (Flask)

Navigate to the server folder:
```
cd server
```

Create a virtual environment and activate it:
```
pipenv install && pipenv shell
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the backend server:
```
flask run --port 5555
```

✅ The backend will now run at http://localhost:5555

3️⃣ Frontend Setup (React + Vite)

Navigate to the React app:
```
cd ../clinic-appointment
```

Install dependencies:
```
npm install
```

Run the development server:
```
npm run dev
```

✅ The frontend will now run at http://localhost:5173

🔗 Connecting Frontend to Backend

The vite.config.js file is already configured to proxy API calls from React to Flask:
```
export default defineConfig({
  server: {
    proxy: {
      '/api': 'http://localhost:5555',
    },
  },
  plugins: [react()],
})
```

That means:

When React fetches /api/patients, it’s automatically redirected to Flask at http://localhost:5555/api/patients.

📄 Available Pages
Page	Route	Description
🏠 Home	/	Welcome screen
👩‍⚕️ Doctors	/doctors	View list of doctors
👨‍👩‍👧 Patients	/patients	Manage patient records
📅 Appointments	/appointments	Schedule and view appointments
🧠 Example API Endpoints (Flask)
Method	Endpoint	Description
GET	/api/doctors	Get all doctors
POST	/api/doctors	Create a new doctor
GET	/api/patients	Get all patients
POST	/api/patients	Add a patient
GET	/api/appointments	Get all appointments
POST	/api/appointments	Create a new appointment
🧑‍💻 Development Notes

Use React Router for navigation.

Use the Fetch API or Axios for data fetching.

Keep your Flask server running while testing API requests.

You can modify the proxy port in vite.config.js if Flask runs on a different port.

🧾 License

This project is licensed under the MIT License — feel free to use and modify it for educational or professional purposes.

👩‍💼 Authors:

Ann Ngatia
Abdirahman Hussein
Ann Gathoni
David Githehu
Nassur Mohammed

Full Stack Developers (React + Flask),
Moringa School.
