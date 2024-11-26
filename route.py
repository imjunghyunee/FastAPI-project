from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import existing_users
from schemas import User


# Define route for HTTP POST requests to /register
router = APIRouter(
    prefix = "/register"
)
# / (root)가 endpoint가 된 것. 이 경로로의 POST request가 creat_user func.을 trigger
class User(BaseModel):
    id: int
    email: str
    name: str
    password: str
    
@router.post(
    "/",
)
def create_user(
    user: User
):
    for existing_user in existing_users: # 동일한 메일 존재
        if existing_user["email"] == user.email:
            # return {"message": "이미 존재하는 이메일입니다. 다른 이메일을 사용하세요."}
            raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다. 다른 이메일을 사용하세요.") # status_code 400: Bad Request
        
        
        # 회원가입
    user.id = len(existing_users) + 1 # id 부여
        # existing_users.append(user) <- append model object itself.... could cause issue when storing data, etc.
    existing_users.append(user.model_dump()) # pydantic .model_dump(): dictionary 형태로 변환
    return {"message": "회원가입이 완료되었습니다."}
    
""" get_users func."""
@router.get(
    "/users"
)
def get_users():
    return existing_users

def create_test(
    user: User
):
    for existing_user in existing_users:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다. 다른 이메일을 사용하세요.")

    existing_users.append(user.model_dump())
    
    return user