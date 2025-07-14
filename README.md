# Calculator API

A minimalistic calculator REST API built with **Python** and **Flask**, developed with **DevOps best practices** in mind (CI/CD, testing, code quality).

---

## Features

- `GET /add?a=2&b=3` → Returns the sum of `a` and `b`
- `GET /multiply?a=2&b=3` → Returns the product of `a` and `b`
- `GET /divide?a=6&b=2` → Returns the result of `a / b`
- `GET /subtract?a=4&b=2` → Returns the result of `a - b`
- `GET /health' → Returns simple service status (200 OK)

All routes include:
- Input validation
- Division by zero handling
- JSON response format

---

## Testing

This project uses `pytest` for unit testing.

To run tests locally:
`pytest`

Test coverage includes:
- Happy paths for all operations
- Input validation
- Division by zero handling

## CI/CD
GitHub Actions is configured to:
- Run tests on every push
- Enforce code style with flake8
- Fail builds on syntax/style/test errors

Workflow file: `.github/workflows/python-ci.yml'

## Project structure

```
.
├── app.py                # Main Flask application
├── test_app.py           # Unit tests for API
├── requirements.txt      # Project dependencies
└── .github/workflows/
    └── python-ci.yml     # GitHub Actions CI configuration
```

## Code style
We use PEP8 and flake8 for formatting.
To check style locally:
`flake8 .`

## How to use

1. Run the app:
`python app.py`
2. Send a request:
```
GET /multiply?a=3&b=4
Response: { "result": 12.0 }
```

### Run with Docker

Build and run the container:
```
docker build -t calculator-api .
docker run -p 5000:5000 calculator-api
```

## Built with
- Python 3.10+
- Flask
- Pytest
- Github Actions
- flake8

## TODO
- [x] /divide endpoint with input validation
- [x] Return 400 if division by zero
- [x] Add test for /divide
- [x] Add /subtract endpoint
- [x] Add tests for /subtract
- [x] Add negative test case for /multiply
- [x] Implement `/health` endpoint
- [x] Add logging to all routes
- [x] Containerize the application with Docker
 
## Author
Developed by Ezmert13 as part of a DevOps learning journey.
