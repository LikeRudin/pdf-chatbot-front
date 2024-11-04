from dataclasses import dataclass
from typing import Dict, Any, Optional 
from requests import Response
from requests.exceptions import JSONDecodeError, RequestException

## 응답 키 상수
SUCCESS = "success"
MESSAGE = "message"
DATA = "data"
ERRORS = "errors"
STATUS_CODE = "status_code"



@dataclass
class ResponseDict:
    success: bool
    message: str
    data: Dict[str, Any]
    errors: Optional[Dict[str, Any]] = None
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        if key in self.__dict__:
            return self.__dict__.get(key, default)
        return default



def transfer_response(response: Response, success_message= "Request success", error_message  ="Request Failed") -> ResponseDict:
    try:
        result = response.json()
        success = result.get(SUCCESS, False)
        message = result.get(MESSAGE, success_message if result.get("success", False) else error_message)
        data = result.get(DATA, {})
        errors = result.get(STATUS_CODE, None)
      
        return ResponseDict(
            success=success,
            message=message,
            data=data,
            errors=errors,
        )
    except JSONDecodeError:
        return ResponseDict(
            success=False,
            message="Invalid Response Data. please tell this issue to backend engineer",
            data={},
            errors=None,
        )
    except RequestException as e:
        return ResponseDict(
            success=False,
            message="unknow exception occured while handling request",
            data={},
            errors={"details": str(e)},
        )
   
def create_failed_response(message:Optional[str], data:Optional[any] ):
    defaultMessage = "Request and Response was successful, but this action cannot process proper functionality"
    return ResponseDict(
            success=False,
            message=defaultMessage + message,
            data=data if data else {},
            errors=None,
        )