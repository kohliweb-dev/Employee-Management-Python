from fastapi import FastAPI,Depends,Query,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import Base, engine, get_db
import models
import schemas

app = FastAPI()

# "Look at the models I created and create the required tables in my SQLite database."
Base.metadata.create_all(bind=engine) 

@app.get("/")
def home():
    return{"message":"Employee Management api is here"}


# this is get method how show the whole  employees data
@app.get("/api/employees")
def get_employees(
    department: str = Query(None, min_length=1, description="Search by department"),
    db: Session = Depends(get_db)
):
    if department:
        employees = db.query(models.Employee).filter(
            models.Employee.department == department
        ).all()
    else:
        employees = db.query(models.Employee).all()

    return employees  

# this is for find employee by id
@app.get("/api/employees/{id}")
def get_employee_by_id(id:int,db:Session=Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


    
# the post method start from here
@app.post("/api/employees", response_model=schemas.EmployeeResponse,status_code=201)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    try:
        new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary,
        joining_date=employee.joining_date,
        is_active=employee.is_active
        )
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    except IntegrityError:
        db.rollback()  ## It means: "Cancel/undo the failed database transaction and return the database session to a usable state."
        raise HTTPException(
        status_code=400,
        detail="Email already exists"
        )



# for updates code start from 

@app.put("/api/employees/{id}")
def update_employee(id:int,employee: schemas.EmployeeCreate,db:Session=Depends(get_db)):

    db_employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")  
        
    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.salary = employee.salary
    db_employee.joining_date = employee.joining_date
    db_employee.is_active = employee.is_active

    db.commit()
    db.refresh(db_employee)

    return db_employee


# for delete the employee details the code start from hehrh

@app.delete("/api/employees/{id}")
def delete_employee(id:int,db:Session=Depends(get_db)):
    employee_db = db.query(models.Employee).filter(models.Employee.id == id).first()
    if employee_db:
        db.delete(employee_db)
        db.commit()
        return "employee delete succesfully"

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


