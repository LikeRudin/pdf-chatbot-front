import streamlit as st

from apis.conversation import send_message

def message_input(placeholder, conversation_pk):
    message = st.chat_input(f"{placeholder}")
    if message: 
        send_message(message=message,pk=conversation_pk)
