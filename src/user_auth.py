import json
import os
import hashlib

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_login(username, password):
    users = load_users()
    hashed = hash_password(password)
    return username in users and users[username] == hashed

def create_account(username, password):
    users = load_users()
    if username in users or username == '':
        return False  #User already exists
    users[username] = hash_password(password)
    save_users(users)
    return True