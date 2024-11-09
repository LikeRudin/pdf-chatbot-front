import streamlit as st

from .session import request_session

from libs import transfer_response
from constants import SESSION_STATE_KEY

API_BASE_URL = "/keys"

def get_api_keys():
    response = request_session.get(f"{API_BASE_URL}")
    result = transfer_response(response)
    
    if result.success:
        st.session_state[SESSION_STATE_KEY.API_KEY_LIST] = result.get("data", [])
        st.session_state[SESSION_STATE_KEY.CURRENT_API_KEY_ID] = result.get("data", False)
    return result

def enroll_api_key(name, api_key, kind):
    response = request_session.post(f"{API_BASE_URL}", json={"name": name, "api_key": api_key, "kind": kind})
    result = transfer_response(response, success_message="Successfully enrolled Key", error_message="Successfully enrolled Key")
    if result.success:
         get_api_keys()
    return result

def delete_api_key(id):
    response = request_session.delete(f"{API_BASE_URL}/{id}")
    result = transfer_response(response, success_message="API key deleted successfully", error_message="Failed to delete API key.")
    if result.success:
         get_api_keys()
    return result