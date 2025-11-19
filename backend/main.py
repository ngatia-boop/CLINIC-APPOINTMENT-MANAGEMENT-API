from backend import create_app
from flask_cors import CORS

app = create_app()
CORS(app, origins=["https://clinic-appointment-management-api-v.vercel.app/"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5555, debug=True)
