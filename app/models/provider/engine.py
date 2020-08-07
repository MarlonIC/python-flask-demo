from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@127.0.0.1:3306/alembic', echo=True)
session_maker = sessionmaker(bind=engine)
session = session_maker()

Base = declarative_base()
