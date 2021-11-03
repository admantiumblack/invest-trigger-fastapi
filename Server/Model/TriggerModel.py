### Package Import ###
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
### AppCode Import ###
from Server.config.DBConfig import db_config
from Server.Schema.TriggerSchema import TriggerSchemaDTO

#########################################################
triggers = Table(
    'TradeSignal', db_config.metadata,
    Column('signalId', Integer, primary_key=True),
    Column('userId', Integer),
    Column('pair', String(12)),
    Column('timeframe', String(10)),
    Column('indicator1', String(11)),
    Column('indicatorVar1', Integer),
    Column('comparator', String(2)),
    Column('indicator2', String(11)),
    Column('indicatorVar2', Integer),
)
##########################################################
def get_user_triggers(userId):
    con = db_config.get_connection()
    result = con.execute(triggers.select().where(
        triggers.c.userId == userId)).fetchall()
    return result
##########################################################
def delete_trigger(userId, signalId):
    con = db_config.get_connection()
    try:
        con.execute(triggers.delete().where(
        triggers.c.userId == userId).where(
            triggers.c.signalId == signalId))
    except:
        return 'delete failed'
    return 'delete success'
##########################################################
def insert_trigger(triggerDict):
    con = db_config.get_connection()
    con.execute(triggers.insert().values(**triggerDict))
##########################################################
def get_all_triggers(timeframe):
    con = db_config.get_connection()
    res = con.execute('''SELECT u.Email, ts.pair, ts.timeframe, 
    ts.indicator1, ts.indicatorVar1, ts.comparator, ts.indicator2, 
    ts.indicatorVar2 
    FROM `TradeSignal` as ts JOIN `user` as u ON u.UserId = ts.userId
    WHERE ts.timeframe = ":timeframe";''', timeframe=timeframe).fetchall()
    return res