import streamlit as st

from agents.clients import get_clients
from agents.calendar import create_calendar, generate_strategy_insight
from agents.export import export_pdf

from services.db import init_db, save_history, load_history


init_db()

st.set_page_config(page_title="AI Content Agency", layout="wide")

st.title("🔥 AI Content Agency Dashboard")


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


# ---------------- HISTORY ----------------
history = load_history()


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


st.sidebar.write("📌 Active:", client["name"])
st.sidebar.write("🎯 Niche:", client["niche"])


# ---------------- GENERATE ----------------
if st.button("🚀 Generate Strategy"):

    with st.spinner("AI is building strategy..."):
        new_calendar = create_calendar(client)

    st.session_state.calendar = new_calendar

    save_history(client["name"], client["niche"], new_calendar)

    st.success("Saved + Generated 🔥")


calendar = st.session_state.calendar


# ---------------- INSIGHTS ----------------
if len(calendar) > 0:

    st.markdown("## 🧠 Strategy Insights")

    insight = generate_strategy_insight(calendar, client["niche"])
    st.info(insight)


# ---------------- EMPTY ----------------
if len(calendar) == 0:
    st.info("👈 Click Generate Strategy")
    st.stop()


# ---------------- WEEKLY PLAN ----------------
st.subheader("📅 Weekly Plan")

i = 0
while i < len(calendar):

    item = calendar[i]

    st.markdown(f"### {item['day']}")
    st.write(item["idea"])
    st.write(item["caption"])
    st.write("Score:", item["score"])

    st.markdown("---")

    i += 1


# ---------------- EXPORT ----------------
pdf_file = export_pdf(calendar)

with open(pdf_file, "rb") as f:
    st.download_button(
        "📥 Download Report",
        f,
        file_name="report.pdf",
        mime="application/pdf"
    )