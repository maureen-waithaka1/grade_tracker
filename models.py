from sqlalchemy import Column, Integer, String, Float # Column is how we define a column in our table
from database import Base # We import Base from own database.py file. Base is the parent class

class Student(Base): # this create a python class called Student. By inheriting from base
    __tablename__ = "students" # this sets the actual name of the table inside the database file

    id = Column(Integer, primary_key=True, index=True)# id is a column in the table, is an integer
    name = Column(String, nullable=False) # nullable = False - means this field is required
    course = Column(String, nullable=False)
    grade = Column(Float, default=0.0) # grade is a column, ad the data type is float, default to 0.0
    email = Column(String, unique=True)
    