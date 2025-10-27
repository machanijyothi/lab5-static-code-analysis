# Lab 5 – Static Code Analysis

## 📘 Overview
This repository contains the implementation and analysis for **Lab 5: Static Code Analysis**.  
The goal is to perform static analysis on a Python file using tools like **Pylint**, **Flake8**, and **Bandit**, identify issues, fix them, and reflect on the improvements.

---

## 📂 Files Included
| File | Description |
|------|--------------|
| `inventory_system.py` | Original code before cleaning |
| `inventory_system_cleaned.py` | Code after fixing style, security, and logic issues |
| `pylint_report.txt` | Pylint analysis report |
| `flake8_report.txt` | Flake8 style analysis report |
| `bandit_report.txt` | Bandit security analysis report |
| `issues_and_fixes.md` | Table listing issues found and how they were fixed |
| `reflection.md` | Reflection on what was learned from the analysis |

---

## 🧠 Tools Used
- **Pylint** – Code quality and linting
- **Flake8** – Style and formatting checks
- **Bandit** – Security vulnerability scanner

---

## 💡 Reflection
See [`reflection.md`](reflection.md) for detailed responses about insights, improvements, and learning outcomes.

---

## ✅ How to Run
```bash
# Run Pylint
pylint inventory_system_cleaned.py

# Run Flake8
flake8 inventory_system_cleaned.py --max-line-length=100

# Run Bandit
bandit -r inventory_system_cleaned.py
