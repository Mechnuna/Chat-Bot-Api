# Тестовое задание

## Mandatory part
Написать Api для чат-бота

### Установка

``git clone git@github.com:Mechnuna/Chat-Bot-Api.git``

### Запуск

**С помощью Makefile**  
``make``

**Вручную поднять Docker-compose**
```
docker-compose up
```
Или
```
pip install -e .
source venv/bin/activate
pip install -e .
uvicorn main:app
```
### SwaggerUI  
И идем на 127.0.0.1:8000/docs 
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

## Bonus part
 
`POST /predict/image` для распознования по фотографии  

Запрос
![bonus_request](img/bonus_request.png)
Ответ
![bonus_responce](img/bonus_responce.png)

**Запуск тестов**  
`pytest test`