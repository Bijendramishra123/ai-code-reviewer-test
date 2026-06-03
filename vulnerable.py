import subprocess

def run_command(user_input):
    # Command injection vulnerability!
    subprocess.call("ping " + user_input, shell=True)

def get_user_age(age_input):
    # No type checking
    age = int(age_input)
    return age

SECRET_KEY = "super-secret-key-12345"
