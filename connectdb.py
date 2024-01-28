from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine,Column,Integer,String
# from sqlalchemy.orm import Session

Base =declarative_base()

#creation of table 
class Usermaster(Base):
    __tablename__='usermaster'
    id =Column(Integer,primary_key=True)
    username =Column(String)
    password =Column(String)

connection_str = "sqlite:///mydb.db"
engine = create_engine(connection_str)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
