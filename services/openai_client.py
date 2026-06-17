import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # 👈 THIS is the magic line


def get_api_key():
    # 1. Try Streamlit Cloud
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except:
        pass

    # 2. Try .env / system env
    key = os.getenv("GROQ_API_KEY")

    if not key:
        raise ValueError("❌ Missing GROQ_API_KEY (check .env or Streamlit secrets)")

    return key


client = Groq(api_key=get_api_key())


def generate(prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content