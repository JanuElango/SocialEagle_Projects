import streamlit as st
import requests

st.set_page_config(page_title="Flask + Streamlit Quiz")

# -----------------------
# LOGIN SECTION
# -----------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            "http://127.0.0.1:5000/login",
            json={"username": username, "password": password}
        )

        if response.json()["status"] == "success":
            st.session_state.logged_in = True
            st.success("Login Successful!")
        else:
            st.error("Invalid Credentials")

# -----------------------
# QUIZ SECTION
# -----------------------

if st.session_state.logged_in:
    st.title("🧠 Python Basics Quiz")

    questions = [
        {"q": "What keyword defines a function?", 
         "options": ["func", "def", "define", "function"],
         "answer": "def"},

        {"q": "Which data type is immutable?", 
         "options": ["list", "set", "tuple", "dict"],
         "answer": "tuple"},

        {"q": "Which symbol is used for comments?", 
         "options": ["#", "//", "--", "/*"],
         "answer": "#"}
    ]

    score = 0

    user_answers = []

    for i, q in enumerate(questions):
        answer = st.radio(q["q"], q["options"], key=i)
        user_answers.append(answer)

    if st.button("Submit Quiz"):
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                score += 1

        st.success(f"Your Score: {score} / {len(questions)}")