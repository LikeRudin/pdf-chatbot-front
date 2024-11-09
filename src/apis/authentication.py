import streamlit as st

from .session import request_session
from libs import transfer_response, create_failed_response
from constants import SESSION_STATE_KEY

API_BASE_URL = "/users"

def login(username:str, password:str) :
    response = request_session.post(f"{API_BASE_URL}/login", json={"username": username, "password": password})
    result = transfer_response(response)
    if result.success:
        token = result.data.get('token', False)
        if not token:
            return create_failed_response(message="Token Not Found")
        st.session_state[SESSION_STATE_KEY.LOGGED_IN] = True
        st.session_state[SESSION_STATE_KEY.TOKEN] = token
        st.session_state[SESSION_STATE_KEY.USERNAME] = username
        request_session.headers.update({"Authorization": f"bearer {token}"})
    return result


def logout():
    token = st.session_state.get('token')
    if token:
        response = request_session.post(f"{API_BASE_URL}/logout")
        result = transfer_response(response=response, success_message="logout complete", error_message="failed to logout")
        if result.success:
            st.session_state.clear()
        return result

def join(username:str, password:str):
    response = request_session.post(f"{API_BASE_URL}/join", json={"username":username, "password":password})

    result = transfer_response(response=response, success_message="welcome", error_message="failed to join")
    if result.success:
        st.session_state[SESSION_STATE_KEY.LOGGED_IN] = True
        user_data = result.data
        st.session_state[SESSION_STATE_KEY.USER] = user_data    
    return result



def refresh_login():
    if SESSION_STATE_KEY.TOKEN in st.session_state:
        token = st.session_state[SESSION_STATE_KEY.TOKEN]
        response = request_session.post(
            f"{API_BASE_URL}/refresh",
            headers={"Authorization": f"Bearer {token}"}
        )
        result = transfer_response(response)
        if result.success:
            new_token = result.data.get("token", False)
            if new_token:
                st.session_state[SESSION_STATE_KEY.TOKEN] = new_token
                request_session.headers.update({"Authorization": f"Bearer {new_token}"})  # 새 토큰으로 헤더 업데이트
             
                return result
            else:
                return create_failed_response(message="Refresh Request Successed. but There is no Token. please tell this issue to backend-engineer")
        else:
            logout()
        return result

