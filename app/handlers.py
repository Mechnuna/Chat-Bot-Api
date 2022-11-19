from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status
from app.forms import UserSendMessage, GetAns
from app.models import connect_db, User, History, Answers, StreamStatus
from app.utils import parse_message, get_last_msg_number

router = APIRouter()


@router.get('/')
def index():
    return {'status': 'OK'}


@router.post('/msg', name='user:get')
def get_message(msg: GetAns = Body(..., embed=True), database=Depends(connect_db)):
    message = database.query(Answers).filter(Answers.id_answer == msg.message,
                                             Answers.type_answer == 'да').one_or_none()
    return {'message': message.text_messages}


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
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User id consists of numbers')
    if user_form.message == r'\start':
        user_msg = user_form.message
        message_number = 0
    else:
        user_msg = get_last_msg_number(user_form.message)
        message_number = get_last_msg_number(user_form, database)
    history_add = History(
        user_id=int(user_form.id),
        text_message=user_msg,
        message_number=message_number + 1,
        type_user=StreamStatus.USER,
    )
    database.add(history_add)
    database.commit()
    return {'id': user.id}

#
# @router.post('/user', name='user:create')
# def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
# 	exists_user = database.query(User.id).filter(User.email == user.email).one_or_none()
# 	if exists_user:
# 		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exists')
# 	new_user = User(
# 		email=user.email,
# 		password=get_password_hash(user.password),
# 		first_name=user.first_name,
# 		last_name=user.last_name,
# 		nickname=user.nickname
# 	)
# 	database.add(new_user)
# 	database.commit()
# 	return {'user_id': new_user.id}
#
#
# @router.get('/user', name='user.get')
# def get_user(token: AuthToken = Depends(check_auth_token), database=Depends(connect_db)):
# 	user = database.query(User).filter(User.id == token.user_id).one_or_none()
# 	return {'id': user.id, 'email':user.email, 'nickname':user.nickname}
