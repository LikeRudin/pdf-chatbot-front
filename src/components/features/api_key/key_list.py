import streamlit as st
from constants import SESSION_STATE_KEY
from apis.key import delete_api_key, get_api_keys

def key_list():
    if SESSION_STATE_KEY.API_KEY_LIST not in st.session_state:
        st.session_state[SESSION_STATE_KEY.API_KEY_LIST] = []
        st.write("There is no api key")
        result = get_api_keys()
        print(result.data)

       
    if SESSION_STATE_KEY.CURRENT_API_KEY_ID not in st.session_state:
        st.session_state[SESSION_STATE_KEY.CURRENT_API_KEY_ID ] 

    api_keys = st.session_state.get(SESSION_STATE_KEY.API_KEY_LIST, [])
    current_key_id = st.session_state.get(SESSION_STATE_KEY.CURRENT_API_KEY_ID, None)
    print(api_keys)
    print("api key")

    if len(api_keys) > 0:
        for key in api_keys:
            left, right = st.columns([6, 2])

            button_type = "primary" if key.get('pk', False) == current_key_id else "secondary"

            if left.button(f"{key['name']} ({key['key_kind']})", key=f"select_{key['pk']}", icon="✏️", type=button_type, use_container_width=True):
                st.session_state['current_key_id'] = key['pk']
                st.rerun()

            if right.button("삭제", key=f"delete_{key['pk']}", icon="❌",  use_container_width=True):
                id = key['pk']
                if id:
                    delete_api_key(id=key['pk'])
                    st.rerun()
