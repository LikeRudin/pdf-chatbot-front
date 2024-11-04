import streamlit as st

from apis.authentication import join

def join_form():
    st.subheader("Join")
    with st.form(key="join_form"):
        username = st.text_input(label="Username", key="join_username")
        password = st.text_input(label="Password", key="join_password", type="password")
        password_confirm = st.text_input(label="Password Confirm", key="join_password_confirm", type="password")
        
        submit_button = st.form_submit_button("Join")
        if submit_button:
            if password == password_confirm: 
                join_result = join(username=username, password=password)
                if join_result == True:
                    st.success(body=f"Conguraturations {username}", icon="✅")
                else:
                    st.error(body="join failed", icon="❌")
            else:
                st.error(body="Password and confirmation do not match", icon="❌")


