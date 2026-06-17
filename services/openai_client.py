import os
from groq import Groq


def get_api_key():
    # Streamlit cloud support
    try:
        import streamlit as st
        return st.secrets["GROQ_API_KEY"]
    except:
        return os.getenv("GROQ_API_KEY")


client = Groq(api_key=get_api_key())


def generate(prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content