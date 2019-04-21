from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


DB_URL = "mysql+mysqlconnector://{u}:{p}@{host}:{port}/{db}".format(
    u=os.environ["MYSQL_USER"],
    p=os.environ["MYSQL_PASSWORD"],
    host="database",
    port=3306,
    db=os.environ["MYSQL_DATABASE"]
    )

def get_engine():
    return create_engine(DB_URL)

def get_session():
    return sessionmaker(bind=get_engine())()
