# ExpenseTracker
NAME = Nsa Churchill Sylvester
MATRIC NO = 24/13852
DEPARTMENT = Computer Science
COURSE = SEN 201

# 📌 Project Overview
ExpenseTracker is a simple Python console-based application that helps users record daily expenses, categorize them, view all recorded expenses, and calculate the total amount spent. All expenses are saved to a file for future access.

This project demonstrates a complete **Software Development Life Cycle (SDLC)** implementation using Python.

---
## 🚀 Features
- Add new expenses with amount, category, and description
- View all saved expenses
- Calculate total expenses
- Persistent storage using a text file (`expenses.txt`)
- Simple, menu-driven console interface

---
## Project Structure
ExpenseTracker/
│
├── main.py
├── expense_manager.py
├── file_handler.py
└── README.md

## 🧠 SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
All phases below strictly use ExpenseTracker names and components.

1️⃣ Requirement Analysis
Functional Requirements
User can:
Add an expense (amount, category, description)
View all expenses
View total amount spent

System should:
Store expenses in a text file
Read saved expenses when viewing records

Non-Functional Requirements:
Python 3
Console-based
Simple, readable, maintainable code

2️⃣ System Design
Architecture:
Modular Python application
Separation of concerns using functions and modules

Component Responsibilities:
main.py = Entry point & user interaction
expense_manager.py = Expense logic & calculations
file_handler.py = File read/write operations

3️⃣ Implementation
expense_manager.py
file_handler.py
main.py

4️⃣ Testing
Test Scenarios
Scenario	Expected Result
Add expense	Expense saved
View expenses	All expenses displayed
View total	Correct sum shown
Restart app	Old expenses still available

✔️ All tested manually through console

5️⃣ Deployment = GitHub

6️⃣ Maintenance
Future improvements:
Add expense deletion
Monthly expense summary
Export to CSV
Add authentication
Build GUI or web version
