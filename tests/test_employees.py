from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# this for get test
def test_get_employees():
    response = client.get("/api/employees")


    assert response.status_code == 200


# this for get_employee_id test
def test_get_employee_by_id():
    response = client.get("/api/employees/1")

    assert response.status_code == 200


# this for employee_create test
def test_create_employees():
    employee = {
        "name": "Test Employee",
        "email": "pytest_employee_987654@example.com",
        "department": "IT",
        "salary": 30000,
        "joining_date": "2026-09-14",
        "is_active": True

    }

    response = client.post("/api/employees", json=employee)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "Test Employee"
    assert data["email"] == "pytest_employee_987654@example.com"
    assert data["department"] == "IT"
    assert data["salary"] == 30000
    assert data["is_active"] is True


# this for update test
def test_update_employee():
    employee = {
        "name": "Updated Employee",
        "email": "pytest_employee_987654@example.com",
        "department": "HR",
        "salary": 40000,
        "joining_date": "2026-09-14",
        "is_active": True
    }

    response = client.put("/api/employees/1",json=employee) 

    assert response.status_code == 200

# this for delete test
def test_delete():
    response = client.delete("/api/employees/1")

    assert response.status_code == 200

