from app.forms import UserSendMessage
from fastapi import Body, Depends
from app.models import connect_db, Answers, History


def get_last_msg_number(user_form: UserSendMessage = Body(..., embed=True), database=Depends(connect_db)) -> int:
    last_message_id = database.query(History).filter(History.user_id == user_form.id, History.type_user
                                                     == 'bot').order_by(History.created_at.desc()).limit(1)
    if last_message_id:
        return last_message_id.message_number
    return 0


def parse_message(message: str):
    ans = None
    if message.lower() in ['yes', 'yeah', 'да', 'конечно', 'ага', 'пожалуй']:
        ans = 'да'
    elif message.lower() in ['no', 'nope', 'неа', 'нет', 'неа', 'найн']:
        ans = 'нет'
    return ans
