from fastapi import FastAPI
from src.routers.parser_router_v1 import router 

app = FastAPI()

app.include_router(router, prefix='/api/v1')
