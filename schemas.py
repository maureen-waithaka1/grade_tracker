from pydantic import BaseModel
from typing import Optional 

# What the user sends to CREATE
# StudentCreate - is the schema for when someone wants to add a new student 
# (name, course, grade, email) - these are the fields they must send in their request
class StudentCreate(BaseModel): 
    name: str
    course: str
    grade: float = 0.0
    email: str

# What the user sends to UPDATE
# StudentUpdate - is for when someone wants to change a student's deatail.
# The key difference is, here everything Optional. 
# Why? Because when updating a user should be able to send just one field and change only that
class StudentUpdate(BaseModel):
    name: Optional[str] = None # name is optional, if not sent, it is None(skip updating it)
    course: Optional[str] = None
    grade: Optional[float] = None


# What the API sends BACK
# StudentResponse is what comes back when someone makes a request
# - notice the Student Respons includes id (because after we create a student, we want
# to tell the user what id they were assigned to)
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str 

    #from_attributes = True - is a bridge between the database world and API world
    # The database gives a SQLAlchemy object. The API needs to return Pydantic schema.
    class config: # special class in pydantic (it ho;ds a configuration settings)
        from_attributes = True # without this line. pydantic cannot read SQLAlchemy model object
