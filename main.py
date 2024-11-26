from fastapi import FastAPI
from route_new import router
import models
from database import engine 

app = FastAPI(
    title = "24-2 백엔드 세션"
)

"""
@app.get("/")
def root():
    return {"message": "Hello World."}"""
    

app.include_router(router)

@app.get("/")

def root():
    return {"message": "Hello World."}

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)