
import streamlit as st
import json
import os

st.title("🧠 Overmind Dashboard")

tabs = st.tabs(["Agent Memory", "Post History", "Chaos Log"])

with tabs[0]:
    st.subheader("Agent Memory (agent_db.json)")
    try:
        data = json.load(open("data/agents_db.json"))
        st.json(data)
    except:
        st.warning("No agent memory file found yet.")

with tabs[1]:
    st.subheader("Post History (posts_log.json)")
    try:
        data = json.load(open("data/posts_log.json"))
        st.json(data)
    except:
        st.warning("No post history found yet.")

with tabs[2]:
    st.subheader("Chaos Logs (chaos_logs.json)")
    try:
        data = json.load(open("data/chaos_logs.json"))
        st.json(data)
    except:
        st.warning("No chaos log found yet.")
