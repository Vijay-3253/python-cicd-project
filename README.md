# Python Employee Management API - CI/CD Learning Project

A small Flask API used to learn Git, GitHub, Pytest, and GitHub Actions.

## 1. Requirements

- Python 3.10 or newer (the GitHub Actions workflow uses Python 3.12)
- Git
- A GitHub account

## 2. Create and activate a virtual environment (Windows)

```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Run the application

```powershell
python app.py
```

The API runs at http://127.0.0.1:5000.

## 5. Try the API

Create an employee:

```powershell
curl.exe -X POST http://127.0.0.1:5000/employees -H "Content-Type: application/json" -d "{\"name\":\"Vijay\",\"role\":\"Python Developer\"}"
```

List employees:

```powershell
curl.exe http://127.0.0.1:5000/employees
```

Get employee 1:

```powershell
curl.exe http://127.0.0.1:5000/employees/1
```

Delete employee 1:

```powershell
curl.exe -X DELETE http://127.0.0.1:5000/employees/1
```

## 6. Run tests locally

Stop the Flask server if it is running, then execute:

```powershell
pytest -v
```

## 7. CI/CD learning workflow

The file `.github/workflows/ci.yml` tells GitHub Actions to:

1. Start a temporary Ubuntu runner.
2. Download the repository.
3. Set up Python 3.12.
4. Install packages from `requirements.txt`.
5. Run the tests with `pytest -v`.

The workflow runs when code is pushed to `main` or when a pull request targets `main`.

## Important learning note

This starter project uses an in-memory Python list instead of a database. Employee data is temporary and resets when the app restarts. We will improve the project as we learn.

## Next steps

1. Run the application locally.
2. Run `pytest -v` and confirm all tests pass.
3. Create a GitHub repository.
4. Push this project to the `main` branch.
5. Open the **Actions** tab on GitHub and inspect the CI run.
