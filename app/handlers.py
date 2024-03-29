from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status
from app.forms import UserSendMessage
from app.models import connect_db, User, History, Answers, StreamStatus
from app.utils import parse_message, get_last_msg_number, check_finish


router = APIRouter()


@router.get('/')
def index():
    return {'status': 'OK'}


@router.post('/message', name='user:message')
def login(user_form: UserSendMessage = Body(..., embed=True), database=Depends(connect_db)):
    user = database.query(User).filter(User.id == user_form.id).one_or_none()
    if not user:
        try:
            user = User(
                id=int(user_form.id)
            )
            database.add(user)
        except ValueError:
            database.rollback()
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User id consists of numbers')
    if user_form.message == r'\start':
        user_msg = user_form.message
        message_number, last_text = 0, None
    else:
        user_msg = user_form.message
        message_number, last_text = get_last_msg_number(user_form, database)
    history_add = History(
        user_id=int(user_form.id),
        text_message=user_msg,
        message_number=message_number,
        type_user=StreamStatus.USER.value,
    )
    database.add(history_add)
    type_answer = parse_message(user_form.message)
    if type_answer:
        msg = database.query(Answers).filter(Answers.id_answer == message_number,
                                             Answers.type_answer == type_answer).one_or_none()
        if msg and not check_finish(last_text, message_number):
            answer_text = msg.text_messages
        else:
            database.rollback()
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='FINISH QUESTION(')
    else:
        answer_text = r'Я тебя не понимаю((Используй Да/Нет или \start'
    database.commit()
    return {'ANSWER': answer_text}
