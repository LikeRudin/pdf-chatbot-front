import streamlit as st

from components.features.auth import login_form,logout_button,join_form
from components.features.api_key import key_list, enroll_api_key_form
from components.features.conversation import create_conversation_form, conversation_control_bar, message_input,message
from apis.conversation import get_conversations

from constants import SESSION_STATE_KEY

if SESSION_STATE_KEY.LOGGED_IN not in st.session_state:
    st.session_state[SESSION_STATE_KEY.LOGGED_IN] = False

is_logged_in = st.session_state.get(SESSION_STATE_KEY.LOGGED_IN, False)

if SESSION_STATE_KEY.CURRENT_CHAT_ID not in st.session_state:
    st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] = False
    
current_conversation_pk = st.session_state.get(SESSION_STATE_KEY.CURRENT_CHAT_ID, False)

if is_logged_in:
    with st.sidebar:
        logout_button()
        with st.expander("API Key List"):
            key_list()
        with st.expander("enroll Open AI Api Key"):
            enroll_api_key_form()
        with st.expander("Start new conversation"):
            create_conversation_form()
        conversations = get_conversations().data
        for a_conversation in conversations:
            conversation_control_bar(title=a_conversation["title"], id=a_conversation["id"])
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

