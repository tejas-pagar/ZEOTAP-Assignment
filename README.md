# Rule Engine Application

This project is a simple 3-tier rule engine application that determines user eligibility based on attributes such as age, department, income, and experience. It uses an Abstract Syntax Tree (AST) to represent and evaluate rules dynamically.

## Features
- Define dynamic rules using AST for flexible conditions.
- Create, modify, and combine rules via API.
- Store and retrieve rules and user data from a database.
- Evaluate user eligibility based on defined rules.

## Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite (local) / PostgreSQL (production)
- **Frontend**: Simple HTML/CSS/JavaScript for user interaction
- **ORM**: Flask-SQLAlchemy

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rule-engine-app.git
cd rule-engine-app
