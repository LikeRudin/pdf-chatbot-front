import streamlit as st

from apis.conversation import create_conversation


def create_conversation_form():
    st.subheader("new Conversation")
    with st.form(key="create_chat_form"):
        title = st.text_input(label="Title", key="chatroom_title")
        submit_button = st.form_submit_button("Create", icon="✔️", type="primary", use_container_width=True)
        if submit_button:
            result = create_conversation(title)
            if result.success:
                st.rerun()
 