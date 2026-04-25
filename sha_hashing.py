# ============================================
# SHA Hashing & Password Salting
# Project: Cryptography Algorithms Implementation
# Tool: hashlib (built-in Python)
# ============================================

import hashlib
import os

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def sha512_hash(message):
    return hashlib.sha512(message.encode()).hexdigest()

def hash_with_salt(password):
    salt = os.urandom(16).hex()
    salted = password + salt
    hashed = hashlib.sha256(salted.encode()).hexdigest()
    return salt, hashed

def verify_password(password, salt, hashed):
    salted = password + salt
    return hashlib.sha256(salted.encode()).hexdigest() == hashed

# --- Demo ---
message = "Hello, Cryptography!"
print(f"Original  : {message}")
print(f"SHA-256   : {sha256_hash(message)}")
print(f"SHA-512   : {sha512_hash(message)}\n")

password = "MySecretPassword123"
print(f"Password  : {password}")
salt, hashed = hash_with_salt(password)
print(f"Salt      : {salt}")
print(f"Hashed    : {hashed}")
print(f"Verified  : {verify_password(password, salt, hashed)}")
print(f"Wrong pwd : {verify_password('wrongpassword', salt, hashed)}")