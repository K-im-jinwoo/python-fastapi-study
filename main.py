from fastapi import FastAPI
from app.routers import common_info_router

app = FastAPI()

app.include_router(common_info_router.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI with Procedures!"}