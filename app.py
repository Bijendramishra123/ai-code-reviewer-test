import sqlite3
import hashlib

# Hardcoded credentials - SECURITY ISSUE!
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

def get_user_data(username):
    # SQL Injection vulnerability!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # DANGEROUS: Direct string concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    data = cursor.fetchall()
    conn.close()
    return data

def hash_password(password):
    # Weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()

def process_payment(amount):
    # No input validation
    result = amount / 0  # Potential division by zero
    return result

unused_variable = "not used"
