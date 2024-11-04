# 🤖📄 Introduction


노마드 코더에서 진행하는 파이썬 10주 스터디의 팀 프로젝트 **PdfChatbot App**의 
프론트엔드 입니다.


Backend Repository: [pdf-chatbot-backend](https://github.com/LikeRudin/pdf-chatbot-backend)

---

## 🚀 Features

1일차 과제
- 🔐 **User Authentication**:로그인, 로그아웃, 회원가입.

---

## 📂 Directory Structure


```
src/
├── apis/                // 백엔드와 통신하기위한 API  
│   └── authenticate.py   // 회원가입, 로그인, 로그아웃 api 함수를 보관 
├── components/          // page를 구성하기 위한  기능 컴포넌트들.  
├── contants.py          // 휴먼-에러를 막기위한 상수 변수들
├── libs                 // 개발 퍈의를 위해 만든 기타 함수들
│   └── responses.py     // 커스텀 response 핸들러 보관
└── home.py              // 엔트리 페이지

```

---

## 💾 Session State data

|name|type|description|
|-----|-----|------|
|logged_in|Boolean| 로그인 여부|
|username|string|현재 로그인한 사용자의 이름 |
|token|string| 인증 토큰|


## 🛠️  Stacks

| Tech        | 
|-------------|
| **Streamlit** | 
| **Python**    | 
| **requests**  | 

---

## 📦 Deployment

아직 로컬에서만 작업중입니다.
- **Streamlit Cloud** 에 배포할 예정

---

## 🛡️ License

MIT
