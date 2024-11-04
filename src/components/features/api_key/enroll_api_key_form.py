import streamlit as st 
from apis.key import enroll_api_key
from components.commons import response_alert


def enroll_api_key_form():
    st.subheader("Open AI API Key")
    with st.form(key="open_ai_api_key"):
        name = st.text_input(label="Key Name", key="name") 
        kind = st.selectbox("API Service Company",("Open AI - GPT4o","Claude - Sonnet"))
        api_key = st.text_input(label="API KEY", type="password", key="api_key")
        submit = st.form_submit_button("Enroll", type="primary", use_container_width=True)
        if submit:
            kind_value = "open_ai" if kind == "Open AI - GPT4o" else "claude"
            result = enroll_api_key(name=name, api_key=api_key, kind=kind_value)
            response_alert(result=result, success_message="succefully enrolled api key", error_message="failed to enroll api key")