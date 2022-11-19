from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute('''create table users (
        id integer not null primary key,
        created_at varchar(256))'''
                    )

    session.execute('''create table history (
        id integer not null primary key,
        user_id integer references users,
        text_message varchar(256),
        message_number integer,
        type_user varchar(10),
        created_at varchar(256));'''
                    )

    session.execute('''create table answers (
        id integer not null primary key,
        id_question integer,
        id_answer integer,
        type_answer varchar(10),
        text_messages varcher(256));'''
                    )
    session.close()


if __name__ == "__main__":
    main()
