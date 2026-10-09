# Habit Tracker API

A REST API built using FastAPI, SQLAlchemy, SQLite, and JWT authentication to manage daily and weekly habits.

## Features

- User registration and login
- Secure password hashing
- JWT authentication
- View current user profile
- Create, list, retrieve, update, and delete habits
- Pagination using skip and limit
- Users can access only their own habits
- Request validation using Pydantic

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- pwdlib

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lavanya3010/habit-tracker-api.git
cd habit-tracker-api
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference. Set your own secret key.

### 5. Run the application

```powershell
uvicorn app.main:app --reload
```

### 6. Open Swagger UI

http://127.0.0.1:8000/docs

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Login and obtain a token |
| GET | `/auth/me` | Get the current user's profile |

### Habits

| Method | Endpoint | Description |
|---|---|---|
| POST | `/habits` | Create a habit |
| GET | `/habits` | List habits with pagination |
| GET | `/habits/{habit_id}` | Get a habit |
| PUT | `/habits/{habit_id}` | Update a habit |
| DELETE | `/habits/{habit_id}` | Delete a habit |

## Security

- Passwords are hashed before storage.
- Protected endpoints require a valid JWT token.
- Users can manage only their own habits.
- Do not upload `.env` or database files containing personal data.

## Author

Lavanya
