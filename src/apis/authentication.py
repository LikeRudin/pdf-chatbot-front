import streamlit as st
import requests

API_BASE_URL = " http://127.0.0.1:8000/api/v1/users"

def login(username, password):
    response = requests.post(f"{API_BASE_URL}/login", json={"username": username, "password": password})

    if response.status_code == 200:
        result = response.json()
        token = result['data']['token']
        st.session_state['logged_in'] = True
        st.session_state['token'] = token
        st.session_state['username'] = username
        return {
            "success": True,
            "message": result['message']
        }

    elif response.status_code == 401:
        result = response.json()
        return {
            "success": False,
            "message": result['message'], 
            "errors": result.get('errors', {}),
        }
    
    else:
        try:
            result = response.json()
            return {
                "success": False,
                "message": result.get('message', 'Unknown error occurred'),
                "errors": result.get('errors', {}),
            }
        except ValueError:
            return {
                "success": False,
                "message": "Invalid response from server",
                "errors": {}
            }


def logout():
    token = st.session_state.get('token')
    if token:
        response = requests.post(f"{API_BASE_URL}/logout")

        if response.status_code == 200:
            st.session_state.clear()
            result = response.json()
            return {
                "success": True,
                "message": result["message"]
            }
        else:
            return {
                "success": False,
                "message": "Failed to log out",
                "errors": response.json().get('errors', {})
            }
    else:
        return {
            "success": False,
            "message": "Even not logged in"
        }


def join(username, password):

    response = requests.post(f"{API_BASE_URL}/join", json={"username":username, "password":password})

    if response.status_code == 201:
        user_data = response.json()
        st.session_state['logged_in'] = True
        st.session_state['user'] = user_data
        return True
    
    return False


