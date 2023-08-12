from fastapi import FastAPI
from fastapi.responses import FileResponse
import databases
from db import database
app = FastAPI()



@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()

@app.get("/file/download")
def download_file():
  return FileResponse(path='data.xlsx', filename='Статистика покупок.xlsx', media_type='multipart/form-data')