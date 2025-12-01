# repository.py
from database.db_connection import execute_query, fetch_query
from database.models import User, Medication, Reminder, Interaction


# USERS

def add_user(user: User):
    query = "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)"
    params = (user.name, user.email, user.password_hash)
    execute_query(query, params)

def get_users():
    query = "SELECT * FROM users"
    return fetch_query(query)


# MEDICATIONS

def add_medication(med: Medication):
    query = "INSERT INTO medications (user_id, name, dosage, frequency) VALUES (%s, %s, %s, %s)"
    params = (med.user_id, med.name, med.dosage, med.frequency)
    execute_query(query, params)

def get_medications_by_user(user_id: int):
    query = "SELECT * FROM medications WHERE user_id = %s"
    return fetch_query(query, (user_id,))

# REMINDERS
def add_reminder(reminder: Reminder):
    query = "INSERT INTO reminders (medication_id, time, status) VALUES (%s, %s, %s)"
    params = (reminder.medication_id, reminder.time, reminder.status)
    execute_query(query, params)

def get_reminders_by_medication(medication_id: int):
    query = "SELECT * FROM reminders WHERE medication_id = %s"
    return fetch_query(query, (medication_id,))


# INTERACTIONS

def add_interaction(interaction: Interaction):
    query = """
    INSERT INTO interactions (medication1, medication2, interaction_level, description)
    VALUES (%s, %s, %s, %s)
    """
    params = (interaction.medication1, interaction.medication2,
              interaction.interaction_level, interaction.description)
    execute_query(query, params)

def get_all_interactions():
    query = "SELECT * FROM interactions"
    return fetch_query(query)

