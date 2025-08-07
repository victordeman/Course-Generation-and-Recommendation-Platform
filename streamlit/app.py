# Streamlit interface for the Course Generation and Recommendation Platform
import streamlit as st
import pandas as pd
from backend.python.recommendation_engine import generate_learning_path

st.title("Course Generation and Recommendation Platform")
st.write("Welcome to the personalized learning platform!")

# Example: Quiz result input
quiz_score = st.slider("Enter your quiz score", 0, 100, 50)
if st.button("Generate Learning Path"):
    path = generate_learning_path(quiz_score)
    st.write(f"Recommended Learning Path: {path['learning_path']}")
