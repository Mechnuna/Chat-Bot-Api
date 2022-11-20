# Тестовое задание

## Задание 1
Написать чат-бота

**Установка**

``git clone git@github.com:Mechnuna/Chat-Bot-Api.git``

**Запуск**

``docker-compose up -d``
Или
```
pip install -e .
source venv/bin/activate
pip install -e .
uvicorn main:app
```

**SwaggerUI**  
И идем на 127.0.0.1:8000  
Запрос вводить в формате:
```
{
  "user_form": {
    "id": "string",
    "message": "string"
  }
}  
```
Запрос
![request](img/post_request.png)
Ответ
![responce](img/post_response.png)
