import subprocess
import os

def run_command(cmd):
    # Command injection
    os.system(cmd)

def delete_file(filename):
    subprocess.call(["rm", "-rf", filename])