import pytest
from app import app, employees


@pytest.fixture
def client():
    # Start each test with an empty employee list.
    employees.clear()

    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

    employees.clear()


def test_get_employees_starts_empty(client):
    response = client.get("/employees")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_employee(client):
    response = client.post(
        "/employees",
        json={"name": "Vijay", "role": "Python Developer"},
    )

    assert response.status_code == 201
    assert response.get_json()["name"] == "Vijay"
    assert response.get_json()["role"] == "Python Developer"


def test_add_employee_requires_name_and_role(client):
    response = client.post("/employees", json={"name": "Vijay"})

    assert response.status_code == 400
    assert response.get_json()["message"] == "Both name and role are required"


def test_get_employee_by_id(client):
    client.post(
        "/employees",
        json={"name": "Vijay", "role": "Python Developer"},
    )

    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Vijay"


def test_get_missing_employee(client):
    response = client.get("/employees/999")

    assert response.status_code == 404
    assert response.get_json()["message"] == "Employee not found"


def test_delete_employee(client):
    client.post(
        "/employees",
        json={"name": "Vijay", "role": "Python Developer"},
    )

    response = client.delete("/employees/1")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Employee deleted"
    assert client.get("/employees/1").status_code == 404
