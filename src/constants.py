from dataclasses import dataclass

@dataclass(frozen=True)
class SessionStateKey:
    LOGGED_IN: str = "logged_in"  # 로그인 여부
    USER : str = "user" # 사용자 데이터
    USERNAME: str = "username"  # 사용자 이름
    TOKEN: str = "token"  # 로그인 토큰
    CURRENT_API_KEY_ID: str = "current_key_id"  # 현재 사용중인 API key ID
    CURRENT_CHAT_ID: str = 'current_chat_id'
    API_KEY_LIST: str = 'api_keys'  # 사용자가 등록한 key 목록
    CONVERSATION_LIST: str = "conversation_list" # 대화목록

SESSION_STATE_KEY = SessionStateKey()

