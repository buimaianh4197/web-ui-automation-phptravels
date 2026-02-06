# PHPTRAVELS Automation Testing Project

This is a project to test the [PHPTRAVELS](https://www.phptravels.net) website automatically. I use **Python**, **Playwright**, and **Pytest**. This project follows the **Page Object Model (POM)** to make it easy to manage.

---

## Tech Stack

- **Python**: The main programming language (version 3.13.9).
- **Playwright**: Used to click, type, and interact with the website.
- **Pytest**: The tool to run and manage test cases.
- **Allure Report**: Used to create beautiful test results.

---

## Project Structure
This project is organized into different folders to keep the code neat:

```text
├── components/          # Reusable UI parts (Navbar, Footer, Login Form)
├── helpers/             # Tools for data generation
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
- **Python**: Download and install it on your PC.
> *Note: If you don't have it, [Dowload here](https://www.python.org/downloads/).*
- **Java**: Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable.
> *Note: If you don't have it, [Dowload here](https://adoptium.net/).*
- **Allure Commandline**: To see the beautiful test reports.
> *Note: If you don't have it, please follow the [Official Install Guide here](https://allurereport.org/docs/v2/install/).*

### 2. Setup
Run these commands in your terminal:

```bash
# Clone the project
git clone https://github.com/buimaianh4197/web-ui-automation-phptravels.git
cd web-ui-automation-phptravels

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
> *Note: All settings (browser, video, screenshots, reports) are already configured in the **pytest.ini** file. Commented commands are to debug, if you need any of them, press `Ctrl + /` it.*

**Run specific tests:**
```bash
pytest -m smoke
```

---

## Reports and Debugging
- `allure-results` will be saved at `reports` folder 
- `playwright-artifacts` will also be saved at `reports` folder and contains evidences as follows:
    - **Screenshots**: A picture is taken for every test.
    - **Videos**: Recorded if a test fails.
    - **Tracing**: Saves a "trace" file when a test fails to help you find bugs.

**To see the report UI:**
```bash
allure serve reports/allure-results
```