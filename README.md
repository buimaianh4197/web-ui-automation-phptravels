# PHPTRAVELS Automation Testing Project

This is a project to test the [PHPTRAVELS](https://www.phptravels.net) website automatically. I use **Python**, **Playwright**, and **Pytest**. This project follows the **Page Object Model (POM)** to make it easy to manage.

---

## Tech Stack

- **Python**: The main programming language.
- **Playwright**: Used to click, type, and interact with the website.
- **Pytest**: The tool to run and manage test cases.
- **Allure Report**: Used to create beautiful test results.
- **Faker**: Used to create random user data (names, emails).

---

## Project Structure
This project is organized into different folders to keep the code neat:

```text
├── components/          # Reusable UI parts (Navbar, Footer, Forms)
├── helpers/             # Tools for random data and Allure reports
├── models/              # Data structures (Signup and Login info)
├── pages/               # Page Objects (Locators and Actions for each page)
├── reports/             # Result files (Allure report, Videos, Screenshots, Trace viewers)
├── tests/               # The actual test cases (Login, Signup)
├── conftest.py          # Main settings for the project
├── pytest.ini           # Default settings for running tests
└── requirements.txt     # List of libraries to install
```

---

## How to Start

### 1. Things you need
- Install **Python** on your PC.
- Install **Allure Commandline** to see the reports.

### 2. Setup
Run these commands in your terminal:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install libraries
pip install -r requirements.txt

# Install browsers
playwright install chromium
```

---

## How to Run Tests

**Run all tests:**
```bash
pytest
```

**Run and see the browser (Headed):**
```bash
pytest --headed
```

**Run specific tests:**

**By Marker:**
```bash
pytest -m smoke
```

**By Name:**
```bash
pytest -k "name_of_test_method"
```

**Generate official Allure report:**
```bash
pytest --official-report
```

---

## Reports and Debugging

- **Screenshots**: A picture is taken for every test.
- **Videos**: Recorded if a test fails.
- **Tracing**: Saves a "trace" file when a test fails to help you find bugs.
- **Masking**: Passwords are hidden in the logs for security.

**To see the report UI:**
```bash
allure serve reports/allure-results
```