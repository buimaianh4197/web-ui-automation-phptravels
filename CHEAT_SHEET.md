# 🚀 Playwright - Pytest - Allure Automation Cheat Sheet

A quick reference guide for running automation tests in this project.

---

## 🛠 1. Basic Execution (Local Debugging)
| Goal | Command |
| :--- | :--- |
| **Headed Mode** (See the browser) | `pytest --headed` |
| **Slow Motion** (Delay in ms) | `pytest --headed --slowmo 1000` |
| **Stop at first failure** | `pytest -x` |
| **Show print statements** | `pytest -s` |
| **Run only last failed tests** | `pytest --lf` |
| **Jump to Debugger (PDB)** | `pytest --pdb` |
| **Verbose Output** | `pytest -v` |
| **List tests only** (Dry run) | `pytest --collect-only` |

---

## 🌐 2. Browser & Device Configuration
| Goal | Command |
| :--- | :--- |
| **Run on Chromium** | `pytest --browser chromium` |
| **Run on Firefox** | `pytest --browser firefox` |
| **Run on WebKit (Safari)** | `pytest --browser webkit` |
| **Emulate iPhone 13** | `pytest --device="iPhone 13"` |
| **Multi-browser test** | `pytest --browser chromium --browser firefox` |

---

## 📊 3. Allure Reporting & Output Summaries
| Step / Goal | Command |
| :--- | :--- |
| **Run & Save Results** | `pytest --alluredir=./allure-results` |
| **Serve Report (Temp)** | `allure serve ./allure-results` |
| **Short Summary Report** | `pytest -rA` (Show summary for all at the end) |
| **Extra Info on Fail/Skip**| `pytest -ra` (Show summary for everything except passed) |
| **Build Static Report** | `allure generate ./allure-results -o ./allure-report --clean` |
| **Clear old results** | `pytest --alluredir=./allure-results --clean-alluredir` |

---

## ⚡ 4. Performance & Parallel Execution
| Goal | Command |
| :--- | :--- |
| **Parallel Execution** | `pytest -n auto` (Uses all CPU cores) |
| **Group by Scope** | `pytest -n auto --dist loadscope` (Ensures tests in same class/file run on same worker) |
| **Record Trace** | `pytest --tracing retain-on-failure` |
| **Capture Screenshot** | `pytest --screenshot only-on-failure` |
| **Record Video** | `pytest --video on-first-retry` |
| **Check Slowest Tests** | `pytest --durations=10` |

---

## 🏷️ 5. Filtering & Tagging
| Goal | Command |
| :--- | :--- |
| **Run by Marker** | `pytest -m smoke` |
| **Exclude Marker** | `pytest -m "not slow"` |
| **Search by Name** | `pytest -k "login_feature"` |

---

## 🛠 6. Maintenance & Advanced Debugging
| Goal | Command |
| :--- | :--- |
| **Retry Flaky Tests** | `pytest --reruns 3 --reruns-delay 1` |
| **Step-wise Execution** | `pytest --sw` (Resumes from last failure) |
| **Show Fixture Order** | `pytest --setup-show` (Debug setup/teardown) |
| **Show Local Variables** | `pytest -l` (Shows variable values on failure) |

---

## 🤖 7. Playwright Native Tools
| Goal | Command |
| :--- | :--- |
| **Record Test Script** | `playwright codegen <url>` |
| **Open Trace Viewer** | `playwright show-trace path/to/trace.zip` |

---

## 💡 Pro-Tips / Common Combinations

### 🕵️ Full Debug Mode
```bash
pytest --headed --slowmo 500 -x -s --tb=short