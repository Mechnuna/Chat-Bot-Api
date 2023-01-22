# Тестовое задание
<a href="https://codeclimate.com/github/Mechnuna/Chat-Bot-Api/maintainability"><img src="https://api.codeclimate.com/v1/badges/c11b7aa9c8db1637bd77/maintainability" /></a>
<a href="https://codeclimate.com/github/Mechnuna/Chat-Bot-Api/test_coverage"><img src="https://api.codeclimate.com/v1/badges/c11b7aa9c8db1637bd77/test_coverage" /></a>
[![ Лицензия MIT ](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![ Размер ](https://img.shields.io/github/repo-size/mechnuna/Chat-Bot-Api)

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
![request](image/post_request.png)
Ответ
![responce](image/post_response.png)

## Bonus part
-> develop tensorflow-api

## Запуск тестов
`pytest test`