import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8000/students"

st.set_page_config(page_title="Student Management System", page_icon="🎓")
st.title("Student Management System")
st.write("Add, view, and delete student records.")

st.subheader("Add a student")
with st.form("add_student_form"):
    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=5, max_value=100, step=1)
    email = st.text_input("Email")
    marks = st.number_input("Marks", min_value=0.0, max_value=100.0,
                            value=0.0, step=0.5)
    submitted = st.form_submit_button("Add Student")

if submitted:
    payload = {
        "id": int(student_id),
        "name": name.strip(),
        "age": int(age),
        "email": email.strip(),
        "marks": float(marks)
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 201:
            st.success("Student added successfully!")
        else:
            try:
                detail = response.json().get("detail", response.text)
            except ValueError:
                detail = response.text
            st.error(f"Could not add student: {detail}")
    except requests.RequestException as exc:
        st.error(f"Could not connect to FastAPI. Is the API running? ({exc})")

st.subheader("All students")
try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    students = response.json()

    if students:
        df = pd.DataFrame(students)
        st.dataframe(df, use_container_width=True, hide_index=True)
        average = df["marks"].mean()
        st.metric("Average marks", f"{average:.2f}")
    else:
        st.info("No students have been added yet.")
except requests.RequestException as exc:
    st.error(f"Could not load students. Start the FastAPI server first. ({exc})")

st.subheader("Delete a student")
with st.form("delete_student_form"):
    delete_id = st.number_input("Student ID to delete", min_value=1,
                                step=1, key="delete_id")
    delete_submitted = st.form_submit_button("Delete Student")

if delete_submitted:
    try:
        response = requests.delete(f"{API_URL}/{int(delete_id)}", timeout=10)
        if response.ok:
            st.success("Student deleted successfully.")
            st.rerun()
        elif response.status_code == 404:
            st.warning("Student not found.")
        else:
            st.error(f"Delete failed: {response.text}")
    except requests.RequestException as exc:
        st.error(f"Could not connect to FastAPI. ({exc})")
