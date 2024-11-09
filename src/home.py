import streamlit as st

from components.features.auth import login_form,logout_button,join_form
from components.features.api_key import key_list, enroll_api_key_form
from components.features.conversation import create_conversation_form, conversation_list, message_input

from constants import SESSION_STATE_KEY


def init():
    if SESSION_STATE_KEY.LOGGED_IN not in st.session_state:
        st.session_state[SESSION_STATE_KEY.LOGGED_IN] = False
    if SESSION_STATE_KEY.CURRENT_CHAT_ID not in st.session_state:
        st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] = False
    if SESSION_STATE_KEY.CURRENT_API_KEY_ID not in st.session_state:
        st.session_state[SESSION_STATE_KEY.CURRENT_API_KEY_ID] = False

init()


is_logged_in = st.session_state.get(SESSION_STATE_KEY.LOGGED_IN, False)

if is_logged_in:
    with st.sidebar:
        logout_button()
        with st.expander("API Key List"):
            key_list()
        with st.expander("enroll Open AI Api Key"):
            enroll_api_key_form()
        with st.expander("Start new conversation"):
            create_conversation_form()
        conversation_list()
    st.title("Make some conversations!")
    current_conversation_pk = st.session_state.get(SESSION_STATE_KEY.CURRENT_CHAT_ID, False)
    message_input(placeholder="Have any Question?", conversation_pk=current_conversation_pk)
        
else :
    st.markdown("""
             <style>
             .stSidebar{
             display:none;
             }
             </style>""",
             unsafe_allow_html=True)
    login_tab, join_tab = st.tabs(["Login", "Join"])
    with login_tab:
        login_form()
    with join_tab:
        join_form()

