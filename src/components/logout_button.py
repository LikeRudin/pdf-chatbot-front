import streamlit as st 
from time import sleep

from apis.authentication import logout

def logout_button():
    logout_click = st.button("Logout", icon="🔚")
    if logout_click:
        response = logout()
        if response["success"]:
            st.success(response["message"])
            sleep(1)
            st.rerun()
        else:
            st.error(response["message"])
