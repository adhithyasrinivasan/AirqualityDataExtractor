from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
async def login():
    return "Logged in"

@router.get("/")
async def root():
    return {"message": "Hello World in login"}