from backend import create_app
from flask_cors import CORS

app = create_app()

# Enable CORS for your frontend
CORS(app, origins=[
    "http://localhost:5173",  # local frontend dev
    "https://clinic-appointment-management-api-v.vercel.app"  # Vercel frontend
])

if __name__ == "__main__":
    # Run on port 5555 to match your old server
    app.run(host="127.0.0.1", port=5555, debug=True)
