import streamlit as st

from components.login_form import login_form
from components.join_form import join_form

login_tab, join_tab = st.tabs(["Login", "Join"])

with login_tab:
    login_form()

with join_tab:
    join_form()