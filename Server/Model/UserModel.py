### Package Import ###
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
### AppCode Import ###
from Server.config.DBConfig import db_config
from Server.Schema.UserSchema import UserSchemaDTO

###############################################################################
users = Table(
    'user', db_config.metadata,
    Column('UserId', Integer, primary_key=True),
    Column('FullName', String(255)),
    Column('Username', String(255)),
    Column('Email', String(255)),
    Column('Password', String(255))
)
###############################################################################
def user_login(user:UserSchemaDTO):
    conn = db_config.get_connection()

    userResult = conn.execute(users.select().where(
        users.c.Username == user.username)
    .where(users.c.Password == user.password)).fetchall()
    return userResult

###############################################################################
def register_user(userProfile:dict):
    conn = db_config.get_connection()
    try:
        conn.execute(users.insert().values(
            **userProfile
        ))
    except:
        print('db error')
        raise Exception()

###############################################################################
def update_profile(userId:int, userProfileDict:dict):
    conn = db_config.get_connection()
    try:
        conn.execute(users.update().values(
        **userProfileDict
        ).filter(users.c.UserId == int(userId)))
    except:
        raise Exception()
###############################################################################
def get_username(username: str):
    conn = db_config.get_connection()
    userResult = conn.execute(users.select().where(
        users.c.Username == username)).fetchall()
    return userResult
###############################################################################
def get_email(email: str):
    conn = db_config.get_connection()
    userResult = conn.execute(users.select().where(users.c.Email == email)).fetchall()
    return userResult