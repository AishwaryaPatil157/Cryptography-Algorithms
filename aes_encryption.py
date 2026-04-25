# ============================================
# AES Encryption & Decryption
# Project: Cryptography Algorithms Implementation
# Tool: PyCryptodome
# ============================================

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    encrypted_text = base64.b64encode(encrypted).decode()
    return iv, encrypted_text

def decrypt_message(iv, encrypted_text, key):
    iv = base64.b64decode(iv)
    encrypted = base64.b64decode(encrypted_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode()

# Generate a random 256-bit key
key = get_random_bytes(32)

message = "Hello! This is a secret message."
print(f"Original Message : {message}")

iv, encrypted = encrypt_message(message, key)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt_message(iv, encrypted, key)
print(f"Decrypted Message: {decrypted}")