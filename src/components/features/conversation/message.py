import streamlit as st

def message(message, role):
    with st.chat_message(role):
        st.write(message)