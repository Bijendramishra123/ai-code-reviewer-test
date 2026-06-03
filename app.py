cat > app.py << 'EOF'
import sqlite3
import hashlib

# Hardcoded credentials
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

def get_user(username):
    # SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(password):
    # Weak MD5
    return hashlib.md5(password.encode()).hexdigest()

def divide(a, b):
    # No validation
    return a / b
EOF# Trigger review
