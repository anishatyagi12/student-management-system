# Student Management System

A beginner-friendly mini project built with Python, SQLite, Pydantic, FastAPI,
Streamlit, and Git. It supports adding, viewing, and deleting students and
shows the average marks of all students.

## Features

- Add a student using the Streamlit form.
- Validate student name, age, email, and marks with Pydantic.
- Store records in a local SQLite database (`students.db`).
- View all students and an individual student through the API.
- Delete a student through the Streamlit app or API.
- Display average marks in the Streamlit app.
- Explore and test API endpoints using FastAPI Swagger documentation.

## Project structure

```text
student_management/
├── database.py
├── models.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `students.db` file is created automatically when the FastAPI application
starts. It is ignored by Git because it is a local runtime database.

## Requirements

- Python 3.10 or newer
- pip
- Git

## Setup

Open a terminal in the project folder.

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the FastAPI backend

Keep this terminal open:

```bash
python -m uvicorn main:app --reload
```

FastAPI runs at <http://127.0.0.1:8000>.

Interactive API documentation: <http://127.0.0.1:8000/docs>.

### 4. Start the Streamlit frontend

Open a second terminal in the same project folder, activate the same virtual
environment, and run:

```bash
streamlit run streamlit_app.py
```

Streamlit normally opens at <http://localhost:8501>.

Keep both servers running while using the application.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students` | Add a student |
| GET | `/students` | List all students |
| GET | `/students/{student_id}` | Get one student |
| DELETE | `/students/{student_id}` | Delete a student |

Example JSON for `POST /students`:

```json
{
  "id": 101,
  "name": "Anisha",
  "age": 21,
  "email": "anisha@example.com",
  "marks": 85.5
}
```

Pydantic validates that the name has at least 2 characters, age is between
5 and 100, email is a valid email address, and marks are between 0 and 100.
Marks default to `0` if omitted.

## Push the project to GitHub

Create an empty public repository on GitHub (do not add a README there if you
already have this local README). Then run these commands from this folder,
replacing the URL with your own repository URL:

```bash
git init
git add .
git commit -m "Initial commit: student management setup"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-management.git
git push -u origin main
```

Make at least two more meaningful commits, for example:

```bash
git add main.py database.py models.py
git commit -m "Add FastAPI and SQLite student endpoints"
git push

git add streamlit_app.py requirements.txt README.md .gitignore
git commit -m "Add Streamlit interface and project documentation"
git push
```

Check the repository page on GitHub and confirm that it is set to **Public**
and that at least three commits are visible.

## Screenshots for submission

Capture your own running application:

1. Start FastAPI and open `http://127.0.0.1:8000/docs`. Take a screenshot
   showing the Student endpoints.
2. Start Streamlit and open `http://localhost:8501`. Add at least one sample
   student so the table and average marks are visible. Take a screenshot.
3. Upload both screenshots to your assignment submission or repository.

Do not commit `.env`, virtual environments, `__pycache__`, or local database
files. Do not put passwords or API keys in a public repository.
