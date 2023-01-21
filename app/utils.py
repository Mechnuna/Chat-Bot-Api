from typing import Any
from textblob import TextBlob

from app.forms import UserSendMessage
from fastapi import Body, Depends
from app.models import History, StreamStatus, connect_db


def get_last_msg_number(user_form: UserSendMessage = Body(..., embed=True), database=Depends(connect_db)):
    last_message_id = database.query(History).filter(History.user_id == user_form.id, History.type_user
                                                     == StreamStatus.USER.value).order_by(History.id.desc()).limit('1').one_or_none()
    if last_message_id:
        return last_message_id.message_number + 1, last_message_id.text_message
    return 0, r'\start'


def parse_message(message: str) -> str:
    ans = None
    if message == r'\start':
        return r'\start'
    textBlb = TextBlob(message)
    message = textBlb.correct().lower()
    if message in ['yes', 'yeah', 'да', 'конечно', 'ага', 'пожалуй']:
        ans = 'да'
    elif message in ['no', 'nope', 'неа', 'нет', 'неа', 'найн']:
        ans = 'нет'
    return ans


def check_finish(message: str, message_number: int) -> bool:
    return message == 'нет' and message_number == 2
