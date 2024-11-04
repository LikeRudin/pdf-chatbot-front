import streamlit as st

from time import sleep
from constants import SESSION_STATE_KEY
from apis.conversation import delete_conversation
from components.commons import response_alert


@st.dialog("Change Title")
def rename_dialog(title, id):
    new_title = st.text_input(label="New Title", key=f"new_title_{title}-{id}", value=title)

    rename, cancle = st.columns(2)
    if rename.button("Submit", key=f"new_title_submit{title}-{id}", type="primary", use_container_width=True):
        return
    if cancle.button("Cancel", key=f"new_title_cancle{title}-{id}", use_container_width=True):
        return



@st.dialog("Confirm Delete")
def delete_dialog(title, id):
    st.write(f"Are you sure you want to delete the chatroom: {title}?")

    delete, cancle = st.columns(2)
    
    if delete.button("Delete", key=f"conversation_delete{title}-{id}", type="primary", use_container_width=True):
        response = delete_conversation(pk=id)
        response_alert(response) 
        st.rerun()
            
        
    if cancle.button("Cancel", key=f"conversation_delete_cancle{title}-{id}", use_container_width=True):
        st.rerun()

def select_chat(id):
    st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] = id



def conversation_control_bar(title, id):
    enter_part, menu_part = st.columns([4, 1])
    enter_part.button(
    f"{title}",
    use_container_width=True,
    on_click=lambda: select_chat(id),
    type="primary" if st.session_state[SESSION_STATE_KEY.CURRENT_CHAT_ID] == id else "secondary"
)
    with menu_part.popover("⚙️"):
        st.button("rename", icon="✏️", key=f"{title}-{id}-rename", use_container_width=True, on_click= lambda: rename_dialog(title=title,id=id))
        st.button("delete", icon="❌", key=f"{title}-{id}-delete", use_container_width=True, on_click= lambda: delete_dialog(title=title,id=id))
            


