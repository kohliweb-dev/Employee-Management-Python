# Employee Management API

This is a small Employee Management API built using Python, FastAPI, SQLAlchemy and SQLite.

## Features

The API supports:

* Get all employees
* Get an employee by ID
* Search employees by department
* Create an employee
* Update an employee
* Delete an employee
* Validation for employee data
* Duplicate email handling
* Automated tests using pytest

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Pytest

## Project Structure

```text
python/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── init_db.py
├── employees.db
├── requirements.txt
├── tests/
│   └── test_employees.py
└── README.md
```

## Setup

The virtual environment is located outside the project folder.

Create the virtual environment:

```powershell
python -m venv myenv
```

Activate the virtual environment in the VS Code PowerShell terminal:

```powershell
& C:\for_practice_only\myenv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(myenv) PS C:\for_practice_only\EmployeeManagement\python>
```

Install the required packages:

```powershell
pip install -r requirements.txt
```


## Database Setup

The project uses SQLite.

To create the database tables, run:

```powershell
python init_db.py
```

This creates the required tables in `employees.db`.

## Run the API

Start the FastAPI application using:

```powershell
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

Run the automated tests using:

```powershell
pytest
```

The project contains at least 5 automated tests covering the employee API.

## API Endpoints

| Method | Endpoint                       | Purpose              |
| ------ | ------------------------------ | -------------------- |
| GET    | `/api/employees`               | Get all employees    |
| GET    | `/api/employees/{id}`          | Get employee by ID   |
| GET    | `/api/employees?department=IT` | Search by department |
| POST   | `/api/employees`               | Create employee      |
| PUT    | `/api/employees/{id}`          | Update employee      |
| DELETE | `/api/employees/{id}`          | Delete employee      |

## Database

The application uses SQLite with SQLAlchemy.

The database file is:

```text
employees.db
```

## API Testing

The API can be tested using FastAPI Swagger UI and the exported Postman API collection included with the project.



## Database Setup

The project uses SQLite with SQLAlchemy.

To create the database and required tables, run:

```powershell
python init_db.py
```

The database file is:

```text
employees.db
```

## Run the API

Start the FastAPI application:

```powershell
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

To run the automated tests:

```powershell
pytest
```

The project contains 5 automated tests.

## API Endpoints

| Method | Endpoint                       | Purpose              |
| ------ | ------------------------------ | -------------------- |
| GET    | `/api/employees`               | Get all employees    |
| GET    | `/api/employees/{id}`          | Get employee by ID   |
| GET    | `/api/employees?department=IT` | Search by department |
| POST   | `/api/employees`               | Create employee      |
| PUT    | `/api/employees/{id}`          | Update employee      |
| DELETE | `/api/employees/{id}`          | Delete employee      |

## API Testing

The API can be tested using:

* FastAPI Swagger UI
* Postman

The Postman API collection is included with the project.

## Error Handling

The API handles common errors such as:

* Employee not found → `404`
* Duplicate email → `400`
* Invalid employee data → `400`
