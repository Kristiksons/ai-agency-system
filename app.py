import streamlit as st
import pandas as pd

from agents.clients import get_clients
from agents.calendar import create_calendar
from agents.export import export_pdf


st.set_page_config(page_title="AI Content Agency", layout="wide")

st.title("🔥 AI Content Agency Dashboard")


# ---------------- CLIENTS ----------------
clients = get_clients()

client_names = []
i = 0
while i < len(clients):
    client_names.append(clients[i]["name"])
    i += 1


# ---------------- SESSION STATE ----------------
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


st.sidebar.markdown("---")
st.sidebar.write("📌 Active:", client["name"])
st.sidebar.write("🎯 Niche:", client["niche"])


# ---------------- EMPTY STATE (IMPORTANT UX) ----------------
if len(st.session_state.calendar) == 0:

    st.info("👈 Select a client and generate a strategy to get started")

    st.markdown("### 🚀 What this tool does:")
    st.write("- Generates 7-day content strategy")
    st.write("- Creates hooks, captions, hashtags, scripts")
    st.write("- Ranks best-performing posts")
    st.write("- Exports client-ready PDF report")


# ---------------- GENERATE ----------------
if st.button("🚀 Generate Strategy"):

    with st.spinner("AI is analyzing your client and building strategy..."):

        st.session_state.calendar = create_calendar(client)

    st.success("Strategy generated 🔥")


# ---------------- OUTPUT ----------------
calendar = st.session_state.calendar

if len(calendar) > 0:

    calendar = sorted(calendar, key=lambda x: x["score"], reverse=True)

    # ---------------- BEST POST ----------------
    best = calendar[0]

    st.markdown("## 🔥 Best Performing Post")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.info(best["idea"])
        st.write("📝", best["caption"])
        st.code(best.get("hashtags", ""))

    with col2:
        st.metric("Score", best["score"])
        st.write("📅 Day:", best["day"])
        st.write("⏰ Time:", best.get("best_time", ""))
        st.write("🧠 Why:", best.get("why", "N/A"))

    st.markdown("---")

    # ---------------- ANALYTICS ----------------
    st.subheader("📊 Performance Overview")

    df = pd.DataFrame([
        {"Day": item["day"], "Score": item["score"]}
        for item in calendar
    ])

    st.line_chart(df.set_index("Day"))

    st.markdown("---")

    # ---------------- FULL PLAN ----------------
    st.subheader("📅 Weekly Content Plan")

    i = 0
    while i < len(calendar):

        item = calendar[i]

        with st.container():

            st.markdown(f"### 📅 {item['day']}")

            col1, col2 = st.columns(2)

            with col1:
                st.write("💡 Hook:", item["idea"])
                st.write("📝 Caption:", item["caption"])
                st.code(item.get("hashtags", ""))

            with col2:
                st.write("🎬 Script:", item.get("reel_script", ""))
                st.write("⏰ Best Time:", item.get("best_time", ""))
                st.write("🧠 Why:", item.get("why", ""))
                st.metric("Score", item["score"])

        st.markdown("---")

        i += 1

    # ---------------- EXPORT ----------------
    pdf_file = export_pdf(calendar)

    with open(pdf_file, "rb") as f:
        st.download_button(
            "📥 Download Client Report",
            f,
            file_name="ai_content_report.pdf",
            mime="application/pdf"
        )