import streamlit as st

from .session import request_session

from libs import transfer_response
from constants import SESSION_STATE_KEY

API_BASE_URL = "/conversations"

def get_conversations():
    response = request_session.get(f"{API_BASE_URL}")
    result = transfer_response(response)
    if result.success:
        st.session_state[SESSION_STATE_KEY.CONVERSATION_LIST] = result.get("data", [])
    return result

def create_conversation(title):
    response =  request_session.post(f"{API_BASE_URL}/", json={"title": title})
    result = transfer_response(response)
    if result.success:
        get_conversations()
    return result
    
def delete_conversation(pk):
    response = request_session.delete(f"{API_BASE_URL}/{pk}")
    result = transfer_response(response)
    if result.get("success", False):
        get_conversations()
    
    if result.success and st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] == pk:
        st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] = False
    return result


def send_message(message, pk):
    response = request_session.post(f"{API_BASE_URL}/{pk}/messages", json={"message": message})
    result = transfer_response(response)
    return result