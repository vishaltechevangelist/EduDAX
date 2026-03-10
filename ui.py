import streamlit as st
import requests, os

st.title("EduDAX - Question Generator")

st.sidebar.header("Filters")
class_name = st.sidebar.selectbox("Class", ["class9"])
subject = st.sidebar.selectbox("Subject", ["science"])
chapter = st.sidebar.selectbox("Chapter", ["chapter1"])
question_type = st.sidebar.selectbox("Question Type", ["mcq", "short", "long"])
num_question = st.sidebar.slider("Number of Questions", min_value=1, max_value=10, value=5)

if st.sidebar.button("Generate Questions"):
    payload = {
        "class_name": class_name, 
        "subject": subject, 
        "chapter": chapter,
        "question_type": question_type,
        "num_question": num_question
    }
    response = requests.post("http://localhost:8000/generate-questions", json=payload)
    if response.status_code == 200:
        st.json(response)
    else:
        st.error("Error in generating questions")