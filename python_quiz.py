import streamlit as st

st.set_page_config(page_title="Python Basics Quiz", page_icon="🐍")

st.title("🐍 Python Basics Quiz")
st.write("Answer all 20 questions and click Submit!")

questions = [
    {"q": "1) What is the correct file extension for Python files?",
     "options": [".pt", ".py", ".pyt", ".python"],
     "answer": ".py"},

    {"q": "2) Which keyword is used to define a function?",
     "options": ["func", "define", "def", "function"],
     "answer": "def"},

    {"q": "3) Which data type is immutable?",
     "options": ["list", "dictionary", "set", "tuple"],
     "answer": "tuple"},

    {"q": "4) What does len() function do?",
     "options": ["Adds numbers", "Returns length", "Deletes item", "Prints output"],
     "answer": "Returns length"},

    {"q": "5) Which symbol is used for comments?",
     "options": ["//", "#", "/* */", "--"],
     "answer": "#"},

    {"q": "6) What is the output of: print(2**3)?",
     "options": ["6", "8", "9", "5"],
     "answer": "8"},

    {"q": "7) Which keyword is used for conditional statements?",
     "options": ["loop", "if", "switch", "case"],
     "answer": "if"},

    {"q": "8) Which loop runs at least once?",
     "options": ["for", "while", "do-while", "None in Python"],
     "answer": "None in Python"},

    {"q": "9) What is used to handle exceptions?",
     "options": ["try-except", "if-else", "loop", "def"],
     "answer": "try-except"},

    {"q": "10) Which function converts string to integer?",
     "options": ["str()", "int()", "float()", "bool()"],
     "answer": "int()"},

    {"q": "11) What is a dictionary key-value pair separated by?",
     "options": [":", ";", ",", "="],
     "answer": ":"},

    {"q": "12) Which method adds item to list?",
     "options": ["add()", "insert()", "append()", "push()"],
     "answer": "append()"},

    {"q": "13) What does break do?",
     "options": ["Stops loop", "Skips iteration", "Prints output", "Restarts loop"],
     "answer": "Stops loop"},

    {"q": "14) What does continue do?",
     "options": ["Stops loop", "Skips current iteration", "Ends program", "None"],
     "answer": "Skips current iteration"},

    {"q": "15) What is type of True?",
     "options": ["int", "string", "bool", "float"],
     "answer": "bool"},

    {"q": "16) Which operator is used for equality check?",
     "options": ["=", "==", "!=", "<>"],
     "answer": "=="},

    {"q": "17) Which collection does not allow duplicates?",
     "options": ["list", "tuple", "set", "dictionary"],
     "answer": "set"},

    {"q": "18) What is output of len([1,2,3])?",
     "options": ["2", "3", "1", "Error"],
     "answer": "3"},

    {"q": "19) Which function prints output?",
     "options": ["echo()", "printf()", "print()", "write()"],
     "answer": "print()"},

    {"q": "20) Which keyword is used to create a class?",
     "options": ["class", "object", "define", "struct"],
     "answer": "class"},
]

score = 0
user_answers = []

for i, q in enumerate(questions):
    st.subheader(q["q"])
    answer = st.radio("Choose one:", q["options"], key=i)
    user_answers.append(answer)

if st.button("Submit Quiz"):
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎯 Your Score: {score} / 20")

    if score == 20:
        st.balloons()
        st.write("🔥 Perfect Score! Python Master!")
    elif score >= 15:
        st.write("👏 Excellent Work!")
    elif score >= 10:
        st.write("👍 Good Job! Keep Practicing.")
    else:
        st.write("📚 Practice More and Try Again!")