from fastapi import FastAPI
from src.check_request.api import check_wallet_router
from fastapi_pagination import add_pagination


app = FastAPI()

add_pagination(app)

app.include_router(check_wallet_router)


