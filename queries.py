from datetime import datetime
from database import engine, Session
from models import Student

local_session = Session(bind=engine)

def get_all_students():
    return local_session.query(Student).all()

def create_student(data):
    student = Student(**data, register_date=datetime.now())
    try:
        local_session.add(student)
        local_session.commit()
    except Exception as e:
        local_session.rollback()
        # raise e
    finally:
        local_session.close()
    return student

def get_student_by_id(student_id):
    return local_session.query(Student).filter_by(id=student_id).first()

def update_student(student_id, data):
    student = get_student_by_id(student_id)
    try:
        student.name = data.get("name")
        student.age = data.get("age")
        local_session.commit()
    except Exception:
        local_session.rollback()
    finally:
        local_session.close()
    return student

def delete_student(student_id):
    student = get_student_by_id(student_id)
    try:
        local_session.delete(student)
        local_session.commit()
    except Exception:
        local_session.rollback()
    finally:
        local_session.close()
    return student