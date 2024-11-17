import bcrypt
import os

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)

def save_hashed_password(password_file, password):
    hashed_pw = hash_password(password)
    with open(password_file, "wb") as file:
        file.write(hashed_pw)

def login(password_file):
    if not os.path.exists(password_file):
        print("Password file not found.")
        return False
    
    with open(password_file, "rb") as file:
        stored_password = file.read()
    
    provided_password = input("Enter password: ")
    return verify_password(stored_password, provided_password)

# Run this only once to store the hashed password
if not os.path.exists("instructor_password.hash"):
    save_hashed_password("instructor_password.hash", "your_secure_password")
