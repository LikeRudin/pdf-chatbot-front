import streamlit as st
import requests

API_BASE_URL = " http://127.0.0.1:8000/api/v1/conversations"

from libs import transfer_response
from constants import SESSION_STATE_KEY

def get_conversations():
    response = requests.get(f"{API_BASE_URL}")
    result = transfer_response(response)
    print(result)
    return result

def create_conversation(title):
    response =  requests.post(f"{API_BASE_URL}/", json={"title": title})
    result = transfer_response(response)
    return result
    
def delete_conversation(pk):
    response = requests.delete(f"{API_BASE_URL}/{pk}")
    result = transfer_response(response)
    
    if result.success and st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] == pk:
        st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] = False
    return result


def send_message(message, pk):
    response = requests.post(f"{API_BASE_URL}/{pk}/messages", json={"message": message})
    result = transfer_response(response)
    return result