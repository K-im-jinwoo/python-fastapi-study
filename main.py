from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import common_info_router

app = FastAPI()

origins = [
    "http://localhost:5173", # 리액트 개발 서버 기본 주소 (개발용)
    "http://127.0.0.1:5173", # localhost 와 동일하지만 명시적으로 추가
    # "http://your-react-app.com", # 실제 배포 환경 리액트 앱 주소
    # "*.your-react-app.com", # 와일드카드로 서브도메인 모두 허용 예시
]

app.add_middleware(
    CORSMiddleware, # CORSMiddleware 추가
    allow_origins=origins, # ✨ 위에서 정의한 허용할 출처 목록! ✨
    allow_credentials=True, # 쿠키 등 인증 정보 포함 요청 허용 (필요시)
    allow_methods=["*"], # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"], # 모든 헤더 허용 (Content-Type, Authorization 등)
)

app.include_router(common_info_router.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI with Procedures!"}