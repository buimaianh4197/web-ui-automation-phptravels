# PHPTRAVELS Automation Testing Project

This is an automation project to test the [PHPTRAVELS](https://www.phptravels.net) website. It uses **Python**, **Playwright**, and **Pytest**. We use the **Page Object Model (POM)** to make the code clean and easy to fix.

---

## Tech Stack

- **Language:** Python 3.10+
- **Tool:** Playwright (for web interaction)
- **Runner:** Pytest (for running tests)
- **Report:** Allure Report (for beautiful results)
- **Fake Data:** Faker (for random names/emails)

---

## Project Structure
This project is organized into different folders to keep the code neat:

```text
├── components/          # Small UI parts like Navbar, Footer, and Login Form
├── helpers/             # Tools for random data and Allure reports
├── models/              # Data structures (Signup data, login data)
├── pages/               # Page Objects (Locators and Actions for each page)
├── reports/             # Where test report, videos, trace viewer and screenshots are saved
├── tests/               # The test cases (Login and Signup scenarios)
├── conftest.py          # Main configuration and "hooks" for the project
├── pytest.ini           # Default settings for running tests
└── requirements.txt     # List of libraries to install
```


---

## How to Start

### 1. Prerequisites
- Install **Python** on your computer.
- Install **Allure Commandline** to see the reports.

### 2. Installation
Open your terminal and run these commands:

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