import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("AI Semester Companion")

subject = st.selectbox(
    "Select Subject",
    ["DSA", "DBMS", "OS", "CN", "Python"]
)

question=st.text_input("Ask a question")

if st.button("Submit"):
    prompt = f"""
You are a helpful {subject} tutor.

Answer as a teacher helping a college student.

Question:
{question}
"""
    try:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.write(response.text)

    except Exception:
        st.error(
            "Gemini is currently busy. Please wait a few seconds and try again."
        )
