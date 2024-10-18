import streamlit as st

from apis.authentication import login

def login_form():
    st.subheader("Login")
    with st.form(key="login_form"):
        username = st.text_input(label="Username", key="login_username")
        password = st.text_input(label="Password", key="login_password", type="password")
        submit_button = st.form_submit_button("Login")
        if submit_button: 
            response = login(username=username, password=password)
            if response["success"]:
                st.success(body=response["message"], icon="✅")
            else:
                st.error(body=response["message"], icon="❌")

