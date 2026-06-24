from sqlalchemy import create_engine # create engine is a function that creates the connection
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker # a function that produces database session on demand

DATABASE_URL = "sqlite:///./grades.db" # this string tells the SQLAlchemy where exactly our database lives. "/" means same folder

# the engine is the actual connection to the database. it uses the URL to know where to connect
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# SessionLocal - blueprint for creating session.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base is the parent class for all our database models. class student(Base), SQLAlchemy knows student is database table
Base = declarative_base()


def get_db():
    db = SessionLocal() # creates a fresh database session 
    try:
        yield db # yield gives the session to whoever called get_db and PAUSES here
    finally:
        db.close() # Closes the sessio  amd returns the connection. Cleanup happens

        