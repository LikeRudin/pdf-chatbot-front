import requests
from libs import transfer_response, create_failed_response

import streamlit as st
from constants import SESSION_STATE_KEY
API_BASE_URL = "http://127.0.0.1:8000/api/v1"


"""
TODO 
1. 베포후 API_BASE_URL 변경
2. server에 refresh 넣기
3. Refresh를 작동시키기 위한 default header 추가

"""

class AutoRefreshSession(requests.Session):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.base_url = API_BASE_URL
        self.access_token = None
        self.headers.update({
            "Content-Type": "application/json",
        })
    
    def set_bearer_token(self, access_token: str):
        self.access_token = access_token
        self.headers.update({ "Authorization": f"Bearer {self.access_token}"})
    
    def refresh_token(self):
            response = super().get("/refresh")
            result = transfer_response(response)
            if result.success:
                new_token = result.data.get("token", False)
                if new_token:
                     st.session_state[SESSION_STATE_KEY.TOKEN] = new_token
                     self.headers.update({"Authorization": f"Bearer {new_token}"}) 
            else:
                 st.toast("session expired")
                 st.session_state.clear()
    
    def request(self, method, url, **kwargs):
        response = super().request(method, f"{API_BASE_URL}{url}", **kwargs)
        
        if response.status_code == 401:
            if self.refresh_token():
                kwargs["headers"] = {"Authorization": f"Bearer {self.access_token}"}
                retry_response = super().request(method, url, **kwargs)
                retry_response.raise_for_status()
                return retry_response
            else:
                response.raise_for_status()  
        return response
            
        



request_session = AutoRefreshSession()