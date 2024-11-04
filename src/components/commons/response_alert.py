import streamlit as st

from time import sleep
from libs.responses import ResponseDict

def response_alert(result:ResponseDict, success_message ="success", error_message="fail"):
    if not isinstance(result, ResponseDict):
        raise TypeError("result must be an instance of ResponseDict")
    
    if result.success == True:
        st.success(result.get("message", success_message), icon="✅")
    else:
        st.error(result.get("message", error_message), icon="❌")
    sleep(1)