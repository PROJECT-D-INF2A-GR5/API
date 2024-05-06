from sqlalchemy import create_engine
from database.models import Base
from dotenv import dotenv_values

def create_tables():
    engine = create_engine(dotenv_values(".env")["CONNECTION_STRING"])
    Base.metadata.create_all(engine)