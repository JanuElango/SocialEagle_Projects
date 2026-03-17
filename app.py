import streamlit as st
import pandas as pd
import re
from rag_agent import chat_agent

st.set_page_config(page_title="Incident AI Chatbot", layout="wide")

# ---------- CSS (Professional UI) ----------
st.markdown("""
<style>
.chat-container {
    max-width: 900px;
    margin: auto;
}
.user-msg {
    background-color: #DCF8C6;
    padding: 12px;
    border-radius: 12px;
    margin: 6px;
    text-align: right;
    font-size: 15px;
}
.bot-msg {
    background-color: #F1F0F0;
    padding: 12px;
    border-radius: 12px;
    margin: 6px;
    text-align: left;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Incident AI Assistant")

# ---------- Session ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Table Parser ----------
def try_parse_table(response):
    try:
        if "|" in response and "---" in response:
            lines = response.strip().split("\n")
            lines = [l for l in lines if "---" not in l]

            data = [re.split(r"\s*\|\s*", l.strip("| ")) for l in lines]

            df = pd.DataFrame(data[1:], columns=data[0])
            return df
    except:
        return None

    return None

# ---------- Chat Display ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for chat in st.session_state.chat_history:
    st.markdown(f'<div class="user-msg">🧑 {chat["user"]}</div>', unsafe_allow_html=True)

    table = try_parse_table(chat["bot"])

    if table is not None:
        st.dataframe(table, use_container_width=True)
    else:
        st.markdown(f'<div class="bot-msg">🤖 {chat["bot"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Input ----------
query = st.text_input("Type your message...")

col1, col2 = st.columns([1, 1])

with col1:
    send = st.button("Send")

with col2:
    clear = st.button("Clear Chat")

# ---------- Actions ----------
if send and query:
    with st.spinner("Thinking..."):
        response = chat_agent(query, st.session_state.chat_history)

    st.session_state.chat_history.append({
        "user": query,
        "bot": response
    })

    st.rerun()

if clear:
    st.session_state.chat_history = []
    st.rerun()