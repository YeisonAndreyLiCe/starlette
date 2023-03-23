from database import Base
from sqlalchemy import Column, Integer, String, DateTime
""" 
class Student:
    name:str
    age:int
    register_date:datetime
"""

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    register_date = Column(DateTime())

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, register_date={self.register_date})"