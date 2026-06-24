from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_Student = models.Student(**student.model_dump()) # ** means unpacking
    db.add(db_student) #stage the record. Tells SQLAlchemy 'I want to save this'
    db.commit() # Save to disk. This when the data is actually written to database
    db.refresh(db_Student) # reloads the object from database after saving, (new id)
    return db_Student # return completed student object


# READ one record
def get_student(db: Session, student_id: int):
    return db.query(models. Student).filter(models.Student.id == student_id).first()

# READ ALL record
def get_students(db: Session):
    return db.query(models. Students).all()


# UPDATE a record
def update_student(db: Session, student_id: int, data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items(): 
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student 

# DELETE/REMOVE a record
def delete_student(db: Session, student_id: int):
    # Find the student first. We cannot delete something we have not found
    student = db.query(models.Student).filter(models.Students.id == student_id).first()
    # if not found, return None
    if not student:
        return None
    
    # tells SQLAlchemy to detele this object
   
    db.delete(student)
    # save the deletion to disc
    db.commit()
    return student