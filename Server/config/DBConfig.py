from sqlalchemy import create_engine, MetaData
from Server.config.BaseConfig import Singleton

class DBConfig(metaclass=Singleton):
    
    def __init__(self):
        self.metadata = MetaData()
        self.engine = create_engine("mysql+pymysql://root@localhost:3306/triggerview")
        self.connection = self.engine.connect()
    
    def get_connection(self):
        return self.connection

db_config = DBConfig()