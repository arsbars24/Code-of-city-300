from os import environ
from fastapi import FastAPI

import databases

from databases import Database

database = Database("sqlite:///C:\Users\Arsbars24\OneDrive\Рабочий стол\code_of_city\Code-of-city-300\CODE300.db")
app = FastAPI()


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.post("/test")
async def fetch_data(id: int):
    query = "SELECT * FROM tablename WHERE ID={}".format(str(id))
    results = await database.fetch_all(query=query)

    return  results