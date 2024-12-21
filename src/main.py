from fastapi import FastAPI

api = FastAPI()

@api.get("/cryptocurrencies")
async def get_cryptocurrencies():
    ...


@api.get("/cryptocurrency/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    ...