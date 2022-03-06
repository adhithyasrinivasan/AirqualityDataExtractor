from fastapi import FastAPI
import uvicorn
from src.routers import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__" and __package__ is None:
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=False)