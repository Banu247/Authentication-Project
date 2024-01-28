from cryptography.fernet import Fernet,InvalidToken
from fastapi import HTTPException

# Generate a key for encryption

encryption_key = Fernet.generate_key()

cipher_suite = Fernet(encryption_key)

# Function to encrypt a password

def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password 

# Function to decrypt a password

def decrypt_password(encrypted_password):
    try:
        decrypted_password = cipher_suite.decrypt(encrypted_password)
        return decrypted_password.decode('utf-8')
    except InvalidToken as e:
        raise HTTPException(status_code=401, detail="Invalid token")  

