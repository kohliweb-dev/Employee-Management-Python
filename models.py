from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(255),nullable=False,unique=True)
    department = Column(String(100),nullable=False)
    salary= Column(Numeric(10,2),nullable=False)
    joining_date= Column(Date,nullable=False)
    is_active = Column(Boolean,default=True)