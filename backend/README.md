# Clinic Appointment Management API - Backend

A Flask-based REST API for managing clinic appointments, doctors, patients, and services.

## Tech Stack

- **Framework**: Flask 3.0.3
- **Database**: PostgreSQL (with SQLAlchemy ORM)
- **API**: Flask-RESTful
- **Migrations**: Flask-Migrate (Alembic)
- **CORS**: Flask-CORS
- **Validation**: Marshmallow

## Project Structure

```
backend/
├── app.py                 # Application factory & main Flask app
├── config.py             # Configuration classes (Development, Production, Testing)
├── extensions.py         # Flask extensions initialization (db, migrate, api, cors)
├── models.py             # SQLAlchemy models (Patient, Doctor, Appointment, Service, etc.)
├── seed.py               # Database seeding script
├── requirements.txt      # Python dependencies
├── routes/               # API route blueprints
│   ├── __init__.py
│   ├── patient_routes.py
│   ├── doctor_routes.py
│   ├── appointment_routes.py
│   └── service_routes.py
├── controllers/          # (Optional) Business logic handlers
├── migrations/           # Alembic database migrations
├── env/                  # Virtual environment (committed; for quick setup)
└── .gitignore           # Git ignore rules for backend
```

## Setup & Installation

### 1. Activate Virtual Environment

The backend includes a pre-configured virtual environment at `backend/env/`:

```bash
cd backend
source env/bin/activate
# On Windows (PowerShell): env\Scripts\Activate.ps1
```

### 2. Install Dependencies

If needed, install or upgrade dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure Database

Set up PostgreSQL connection. The default config uses:
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `clinic_db`
- **User**: `postgres`
- **Password**: `githehu123`

To use different credentials, create a `.env` file in `backend/`:

```env
DEV_DATABASE_URL=postgresql://user:password@localhost:5432/clinic_db
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key
```

### 4. Run Migrations

Apply database migrations to create tables:

```bash
cd ..  # Go to project root
flask db upgrade
```

Or from `backend/`:

```bash
cd ..
python -m flask db upgrade
```

### 5. Seed the Database (Optional)

Populate the database with sample data (doctors, patients, services, appointments):

```bash
cd ..  # From project root
python -m backend.seed
```

This creates:
- **3 Doctors**: Alice Smith, Bob Jones, Carol Lee
- **3 Services**: General Checkup, Dental Cleaning, Physical Therapy
- **2 Patients**: John Doe, Jane Avery
- **3 Sample Appointments**

## Running the Server

### Development Server

From the project root (with venv activated):

```bash
cd backend
flask run
```

Server runs on `http://127.0.0.1:5000` by default.

To use a different port:

```bash
flask run --port 5001
```

## API Endpoints

All endpoints are under the `/api` prefix.

### Patients

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients` | List all patients |
| POST | `/api/patients` | Create a new patient |
| GET | `/api/patients/<id>` | Get patient by ID |
| PATCH | `/api/patients/<id>` | Update patient |
| DELETE | `/api/patients/<id>` | Delete patient |

**Example - Create Patient:**
```bash
curl -X POST http://127.0.0.1:5000/api/patients \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "555-1234"
  }'
```

### Doctors

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/doctors` | List all doctors |
| POST | `/api/doctors` | Create a new doctor |
| GET | `/api/doctors/<id>` | Get doctor by ID |
| PATCH | `/api/doctors/<id>` | Update doctor |
| DELETE | `/api/doctors/<id>` | Delete doctor |

**Example - Create Doctor:**
```bash
curl -X POST http://127.0.0.1:5000/api/doctors \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Alice",
    "last_name": "Smith",
    "specialty": "General Practice",
    "phone": "555-0001",
    "service_ids": [1, 2]
  }'
```

### Services

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/services` | List all services |
| POST | `/api/services` | Create a new service |
| GET | `/api/services/<id>` | Get service by ID |
| PATCH | `/api/services/<id>` | Update service |
| DELETE | `/api/services/<id>` | Delete service |

**Example - Create Service:**
```bash
curl -X POST http://127.0.0.1:5000/api/services \
  -H "Content-Type: application/json" \
  -d '{
    "name": "General Checkup",
    "duration_minutes": 30,
    "price": 80.0
  }'
```

### Appointments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/appointments` | List all appointments |
| POST | `/api/appointments` | Create a new appointment |
| GET | `/api/appointments/<id>` | Get appointment by ID |
| PATCH | `/api/appointments/<id>` | Update appointment |
| DELETE | `/api/appointments/<id>` | Delete appointment |

**Example - Create Appointment:**
```bash
curl -X POST http://127.0.0.1:5000/api/appointments \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "service_id": 1,
    "start_time": "2025-11-19T10:00:00",
    "status": "Scheduled"
  }'
```

**Features:**
- Automatic `end_time` calculation based on service duration
- Overlap detection: prevents double-booking doctors
- Status tracking: `Scheduled`, `Completed`, `Cancelled`

## Response Format

All responses are JSON. Success responses include data; error responses include a message.

**Success Example:**
```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "555-1234"
  }
]
```

**Error Example:**
```json
{
  "message": "Patient not found"
}
```

HTTP status codes:
- `200`: Success (GET, PATCH)
- `201`: Created (POST)
- `204`: No Content (DELETE)
- `400`: Bad Request
- `404`: Not Found
- `409`: Conflict (e.g., overlapping appointment)
- `500`: Server Error

## Database Migrations

### Create a New Migration

After editing models, generate a migration:

```bash
cd ..
flask db migrate -m "describe your changes"
```

### Apply Migrations

```bash
cd ..
flask db upgrade
```

### View Migration Status

```bash
cd ..
flask db current    # Show current revision
flask db history    # Show migration history
```

## Testing Routes in Browser

### Via cURL

```bash
# Get all patients
curl http://127.0.0.1:5000/api/patients

# Get all doctors
curl http://127.0.0.1:5000/api/doctors

# Get all services
curl http://127.0.0.1:5000/api/services

# Get all appointments
curl http://127.0.0.1:5000/api/appointments

# Pretty-print JSON (if jq is installed)
curl http://127.0.0.1:5000/api/patients | jq .
```

### Via Browser or REST Client

Open your browser or use Postman/Insomnia:

- **List Patients**: http://127.0.0.1:5000/api/patients
- **List Doctors**: http://127.0.0.1:5000/api/doctors
- **List Services**: http://127.0.0.1:5000/api/services
- **List Appointments**: http://127.0.0.1:5000/api/appointments

## Environment Variables

Configure via `.env` file or system environment:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_APP` | `backend.app:create_app` | App factory entry point |
| `FLASK_ENV` | `development` | Environment (development, production, testing) |
| `FLASK_DEBUG` | `1` | Debug mode (0=off, 1=on) |
| `DEV_DATABASE_URL` | (PostgreSQL default) | Development database URL |
| `DATABASE_URL` | (PostgreSQL default) | Production database URL |
| `TEST_DATABASE_URL` | `clinic_test_db` | Testing database URL |
| `SECRET_KEY` | `your-strong-secret-key` | Flask secret key for sessions |

## Development Workflow

1. **Start server**: `flask run`
2. **Edit models**: Update `backend/models.py`
3. **Create migration**: `flask db migrate -m "description"`
4. **Apply migration**: `flask db upgrade`
5. **Test endpoints**: Use cURL, Postman, or your frontend
6. **Seed data**: `python -m backend.seed` (re-run to reset data)

## Common Issues

### Port 5000 Already in Use

Kill the existing process:

```bash
# macOS/Linux
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

Or use a different port:

```bash
flask run --port 5001
```

### Database Connection Error

Ensure PostgreSQL is running and credentials are correct:

```bash
psql -U postgres -h localhost -p 5432
```

### ImportError: No module named 'backend'

Ensure you're in the project root (one level above `backend/`) when running Flask commands:

```bash
cd ..  # Go to project root
flask run
```

### Relative Import Errors When Running seed.py

Run as a module from the project root:

```bash
cd ..
python -m backend.seed
```

Not:

```bash
cd backend
python seed.py  # ❌ This fails with import errors
```

## Contributing

- Follow PEP 8 style guidelines
- Write tests for new routes
- Document API changes in this README
- Use meaningful commit messages

## License

(Add your license here)

## Support

For issues or questions, contact the development team or create an issue in the repository.
