from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title='CBSE Question Generator')
app.include_router(router)