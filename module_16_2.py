from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Path
from typing import Annotated

# Создаем объект FastAPI
app = FastAPI()

# Маршрут главной страницы
@app.get("/")
def read_main():
    return {"message": "Главная страница"}

# Маршрут страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут страницы пользователя с параметром в пути
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(..., description="Enter User ID", ge=1, le=100)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут страницы пользователя с параметрами в пути
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(..., description="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(..., description="Enter age", ge=18, le=120)]
):
    return {
        "message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"
    }
