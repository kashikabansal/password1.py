import streamlit as st

# Fixed data
div = "div b"
session_taken_by = "abc"
lecture_name = "python"
password_by_sir = 2400

# Streamlit UI
st.title("Lecture Attendance System")

st.write("### Lecture Details")
st.write(f"**Division:** {div}")
st.write(f"**Taken By:** {session_taken_by}")
st.write(f"**Lecture Name:** {lecture_name}")

# User input
password_by_student = st.number_input("Enter the password:", min_value=0, step=1)

# Button to validate password
if st.button("Submit"):
    if password_by_student == password_by_sir:
        st.success("Attendance given ✅")
    else:
        st.error("No attendance for you ❌")
