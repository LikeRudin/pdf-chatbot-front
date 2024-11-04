import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000/api/v1/keys"
from libs import transfer_response
from constants import SESSION_STATE_KEY


def get_api_keys():
    response = requests.get(f"{API_BASE_URL}")
    result = transfer_response(response)
    
    if result.success:
        st.session_state[SESSION_STATE_KEY.API_KEY_LIST] = result.data.get(SESSION_STATE_KEY.API_KEY_LIST, [])
        st.session_state[SESSION_STATE_KEY.CURRENT_API_KEY_ID] = result.data.get(SESSION_STATE_KEY.CURRENT_API_KEY_ID, False)
    return response

def enroll_api_key(name, api_key, kind):
    response = requests.post(f"{API_BASE_URL}", json={"name": name, "api_key": api_key, "kind": kind})
    result = transfer_response(response, success_message="Successfully enrolled Key", error_message="Successfully enrolled Key")
    if result.success:
         get_api_keys()
    return result

def delete_api_key(id):
    response = requests.delete(f"{API_BASE_URL}/{id}")
    result = transfer_response(response, success_message="API key deleted successfully", error_message="Failed to delete API key.")
    if result.success:
         get_api_keys()
    return result