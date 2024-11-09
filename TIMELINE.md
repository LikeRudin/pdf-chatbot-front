## 11.09

- `RequestSession` Class 생성

requests의 설정 정보를 모든 apis 메서드가 공유하도록
request.session을 상속받은 class

`RequestSession`의 instance를 기반으로 다른 모든 api 함수가 동작한다.
서버에 요청을 보낼때 전부 header에 동일한 token을 가지게된다.

로그인시에 다음 함수를 통해 토큰을 저장해주면 된다.
```python

## apis/session
class RequestSession:
    ##..
    ## ..
  def set_bearer_token(self, access_token: str):
        self.access_token = access_token
        self.headers.update({ "Authorization": f"Bearer {self.access_token}"})

## apis/authentications
    request_session.set_bearer_token(token)
``` 

- `Compound` 패턴으로 전환

원래도 compound pattern을 지향하고있었으나, 일부 컴포넌트들이 prop-drilling 방식으로 
사용되고있었기에, 전부 compound pattern으로 변경했다.

