import psycopg2
from sqlalchemy import create_engine
from  ...config.process.parser import config

conn = psycopg2.connect(**config["POSTGRES"])
cur = conn.cursor()
engine = create_engine(config["CONNECTION URL"])


class SaveIntoPostgres():

    def save_entity_into_postgres(self,query, data):
        
        cur.execute(query, data)



class LoadFromPostgres():
    
    def load_entity_from_postgres(self,query, data):

        cur.execute(query, data)
        rows = cur.fetchall()

        return rows