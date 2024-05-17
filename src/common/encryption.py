from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def generate_key(password, salt):
   
    """Generate a symmetric encryption key using PBKDF2HMAC key derivation."""
   
    # Correction: Ensure the password is properly encoded and kdf is correctly imported
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode('utf-8'))  # Ensuring password is bytes

def encrypt_data(plaintext, password):
 
    """Encrypt data using AES-GCM mode."""
 
    plaintext = plaintext.encode('utf-8')  # Ensure plaintext is in bytes
    salt = os.urandom(16)  # Secure random salt
    key = generate_key(password, salt)
    nonce = os.urandom(12)  # Nonce for AES-GCM

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalise()

    # Return concatenated salt, nonce, tag, and ciphertext for proper decryption later
    return salt + nonce + encryptor.tag + ciphertext

def decrypt_data(ciphertext, password):
   
    """Decrypt data encrypted with AES-GCM."""
   
    salt = ciphertext[:16]
    nonce = ciphertext[16:28]
    tag = ciphertext[28:44]
    encrypted_message = ciphertext[44:]  # Correctly isolate the encrypted message
    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
   
    return (decryptor.update(encrypted_message) + decryptor.finalise()).decode('utf-8')  # Decode decrypted bytes to string

# Example usage:

if __name__ == '__main__':
    password = 'my_secure_password'
    message = 'Hello, world!'

    encrypted = encrypt_data(message, password)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_data(encrypted, password)
    print(f"Decrypted: {decrypted}")
