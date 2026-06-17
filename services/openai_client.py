import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


# ---------------- GET API KEY SAFELY ----------------
def get_api_key():
    # 1. Streamlit Cloud secrets
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except:
        pass

    # 2. Local .env / system env
    return os.getenv("GROQ_API_KEY")


api_key = get_api_key()

if not api_key:
    raise ValueError("❌ GROQ_API_KEY missing (add it to .env or Streamlit secrets)")


# ---------------- INIT GROQ CLIENT ----------------
client = Groq(api_key=api_key)


# ---------------- GENERATE FUNCTION ----------------
def generate(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ stable + fast + free tier friendly
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Groq error: {str(e)}"