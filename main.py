from fastapi import FastAPI, HTTPException
from database import create_table, get_connection
from models import Student

app = FastAPI(title="Student Management API")

@app.on_event("startup")
def startup():
    create_table()

@app.post("/students", status_code=201)
def add_student(student: Student):
    try:
        with get_connection() as conn:
            conn.execute(
                """INSERT INTO students (id, name, age, email, marks)
                   VALUES (?, ?, ?, ?, ?)""",
                (student.id, student.name, student.age,
                 str(student.email), student.marks)
            )
            conn.commit()
        return {"message": "Student added successfully",
                "student": student.model_dump()}
    except Exception as exc:
        # SQLite reports a uniqueness/integrity error for duplicate IDs.
        import sqlite3
        if isinstance(exc, sqlite3.IntegrityError):
            raise HTTPException(status_code=409,
                                detail="A student with this ID already exists")
        raise

@app.get("/students")
def get_students():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, name, age, email, marks FROM students ORDER BY id"
        ).fetchall()
    return [dict(row) for row in rows]

@app.get("/students/{student_id}")
def get_student(student_id: int):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, name, age, email, marks FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(row)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE id = ?", (student_id,)
        )
        conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
