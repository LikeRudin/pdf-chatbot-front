import streamlit as st

from components.login_form import login_form
from components.join_form import join_form
from components.logout_button import logout_button

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

with st.sidebar:
    if 'logged_in' in st.session_state and st.session_state['logged_in'] == True:
        logout_button()

login_tab, join_tab = st.tabs(["Login", "Join"])

with login_tab:
    login_form()

with join_tab:
    join_form()
