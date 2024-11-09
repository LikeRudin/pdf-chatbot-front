## 11.09

`RequestSession` 생성

requests의 설정 정보를 모든 apis 메서드가 공유하도록
request.session을 상속받은 class 

`RequestSession`의 instance를 기반으로 다른 모든 api 함수가 동작한다.
서버에 요청을 보낼때 전부 header에 동일한 token을 가지게된다.
