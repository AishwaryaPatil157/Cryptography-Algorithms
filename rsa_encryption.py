# ============================================
# RSA Encryption & Decryption
# Project: Cryptography Algorithms Implementation
# Tool: rsa library
# ============================================

import rsa

# Generate RSA public and private keys (2048-bit)
print("Generating RSA keys...")
public_key, private_key = rsa.newkeys(2048)
print("Keys generated successfully!")

# Message to encrypt
message = "Secure message using RSA encryption."
print(f"\nOriginal Message : {message}")

# Encrypt using public key
encrypted = rsa.encrypt(message.encode(), public_key)
print(f"Encrypted Message: {encrypted.hex()[:60]}...")

# Decrypt using private key
decrypted = rsa.decrypt(encrypted, private_key).decode()
print(f"Decrypted Message: {decrypted}")