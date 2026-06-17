import streamlit as st

from agents.clients import get_clients
from agents.calendar import create_calendar, generate_strategy_insight, regenerate_day
from agents.export import export_pdf
from services.db import init_db, save_history, load_history
from services.openai_client import get_api_key


# ---------------- INIT ----------------
init_db()

st.set_page_config(page_title="AI Agency Dashboard", layout="wide")

st.title("🔥 AI Content Agency Dashboard")


# ---------------- API CHECK ----------------
api_key = get_api_key()

if not api_key:
    st.error("❌ Missing GROQ_API_KEY")
    st.stop()


# ---------------- CLIENTS ----------------
clients = get_clients()

client_names = []
i = 0
while i < len(clients):
    client_names.append(clients[i]["name"])
    i += 1


# ---------------- SESSION ----------------
if "selected_client" not in st.session_state:
    st.session_state.selected_client = client_names[0]

if "calendar" not in st.session_state:
    st.session_state.calendar = []


# ---------------- SIDEBAR ----------------
st.sidebar.header("👥 Clients")

selected = st.sidebar.selectbox(
    "Switch Client",
    client_names,
    index=client_names.index(st.session_state.selected_client)
)

st.session_state.selected_client = selected


# ---------------- GET CLIENT ----------------
client = None
i = 0
while i < len(clients):
    if clients[i]["name"] == st.session_state.selected_client:
        client = clients[i]
    i += 1


st.sidebar.markdown("### 📌 Active Client")
st.sidebar.write(client["name"])

st.sidebar.markdown("### 🎯 Niche")
st.sidebar.write(client["niche"])


# ---------------- HEADER BUTTON ----------------
col1, col2 = st.columns(2)

with col1:
    generate_clicked = st.button("🚀 Generate Strategy", use_container_width=True)

with col2:
    export_clicked = st.button("📥 Export PDF", use_container_width=True)


# ---------------- GENERATE ----------------
if generate_clicked:

    with st.spinner("AI building strategy..."):
        new_calendar = create_calendar(client)

    st.session_state.calendar = new_calendar

    save_history(client["name"], client["niche"], new_calendar)

    st.success("Strategy generated 🔥")


calendar = st.session_state.calendar


# ---------------- INSIGHTS CARD ----------------
if len(calendar) > 0:

    st.markdown("## 🧠 Insights")

    st.info(generate_strategy_insight(calendar, client["niche"]))


# ---------------- EMPTY STATE ----------------
if len(calendar) == 0:
    st.info("Click **Generate Strategy** to start")
    st.stop()


# ---------------- CONTENT GRID ----------------
st.markdown("## 📅 Weekly Content Plan")


i = 0
while i < len(calendar):

    item = calendar[i]

    with st.container():

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### {item['day']}")
            st.write(item["idea"])
            st.write(item["caption"])

        with col2:
            st.metric("Score", item["score"])

            if st.button("🔄 Improve", key=f"regen_{i}"):

                improved = regenerate_day(client["niche"], item["day"])

                if improved:

                    calendar[i]["idea"] = improved["idea"]
                    calendar[i]["caption"] = improved["caption"]
                    calendar[i]["score"] = improved["score"]

                    st.session_state.calendar = calendar

                    st.success("Updated 🔥")
                    st.rerun()

    st.divider()

    i += 1


# ---------------- EXPORT ----------------
if export_clicked:

    pdf_file = export_pdf(calendar)

    with open(pdf_file, "rb") as f:
        st.download_button(
            "⬇️ Download Report",
            f,
            file_name="report.pdf",
            mime="application/pdf"
        )