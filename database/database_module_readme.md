# Database Module

## Overview

This module handles all database operations for the Personalized Medication Reminder & Interaction Checker project. It is built using Python 3.13 and PyMySQL for connecting to a MySQL database.

The module provides:
- User management
- Medication management (now includes `rx_cui`)
- Reminder management (now includes `taken_at` and `next_dose_at`)
- Drug interaction management

All database operations are encapsulated in helper functions to make usage simple and safe.

## Folder Structure

database/
├─ __init__.py
├─ config.py
├─ db_connection.py
├─ models.py
├─ repository.py

## Setup

1. Install PyMySQL:
```
pip install pymysql
```

2. Configure database credentials in `config.py`.

3. Make sure the MySQL server is running and the database `med_app` exists.

## How to Use

### Importing
```python
from database.repository import (
    add_user, get_users,
    add_medication, get_medications_by_user,
    add_reminder, get_reminders_by_medication,
    add_interaction, get_all_interactions
)
from database.models import User, Medication, Reminder, Interaction
```

### Users
```python
# Create a new user
user = User(id=None, name="Alice", email="alice@mail.com", password_hash="hashed_password")
add_user(user)

# Fetch all users
users = get_users()
```

### Medications
```python
# Add a medication for a user
med = Medication(
    id=None,
    user_id=1,
    name="Paracetamol",
    dosage="500mg",
    frequency="2x/day",
    rx_cui="12345"  # NEW
)
add_medication(med)

# Get medications for a user
medications = get_medications_by_user(1)
```

### Reminders
```python
# Add a reminder for a medication
reminder = Reminder(
    id=None,
    medication_id=1,
    time="09:00",
    taken_at=None,       # NEW
    next_dose_at="13:00" # NEW
)
add_reminder(reminder)

# Get reminders for a medication
reminders = get_reminders_by_medication(1)
```

### Interactions
```python
# Add a drug interaction
interaction = Interaction(
    id=None,
    medication1="Paracetamol",
    medication2="Ibuprofen",
    interaction_level="Moderate",
    description="May increase liver risk"
)
add_interaction(interaction)

# Get all interactions
all_interactions = get_all_interactions()
```

## Notes

- All database operations use helper functions `execute_query` and `fetch_query` to manage connections safely.
- This module is fully compatible with Python 3.13 using PyMySQL.
- Any future modules (API integration, core logic, UI) can call these repository functions without worrying about connection management.
- Ensure valid IDs are passed (e.g., `user_id`, `medication_id`) to avoid errors.
- `rx_cui` standardizes medications and `taken_at` / `next_dose_at` track user adherence.