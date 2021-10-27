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
    Column('timeFrame', String(10)),
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