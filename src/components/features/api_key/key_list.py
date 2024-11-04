import streamlit as st
from apis.key import delete_api_key, get_api_keys

def key_list():
    if 'api_keys' not in st.session_state:
        st.session_state['api_keys'] = []
        st.write("There is no api key")
        get_api_keys()
    if 'current_key_id' not in st.session_state:
        st.session_state['current_key_id'] = 1

    api_keys = st.session_state.get('api_keys', [])
    current_key_id = st.session_state.get('current_key_id', None)

    for key in api_keys:
        left, right = st.columns([6, 2])

        button_type = "primary" if key['id'] == current_key_id else "secondary"

        if left.button(f"{key['name']} ({key['provider']})", key=f"select_{key['id']}", icon="✏️", type=button_type, use_container_width=True):
            st.session_state['current_key_id'] = key['id']
            st.rerun()

        if right.button("삭제", key=f"delete_{key['id']}", icon="❌",  use_container_width=True):
            id = key['id']
            if id:
                delete_api_key(id)
                st.rerun()
