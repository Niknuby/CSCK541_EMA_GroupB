from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, key_derivation
from cryptography.hazmat.backends import default_backend
import os

def generate_key(password, salt):
    
    """Generate a symmetric encryption key using PBKDF2HMAC key derivation."""
    
    kdf = key_derivation.kdf.pbkdf2.PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode('utf-8'))

def encrypt_data(plaintext, password):
    
    """Encrypt data using AES-GCM mode."""
    
    salt = os.urandom(16)  # Secure random salt
    key = generate_key(password, salt)
    nonce = os.urandom(12)  # Nonce for AES-GCM

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return salt + nonce + encryptor.tag + ciphertext

def decrypt_data(ciphertext, password):
    
    """Decrypt data encrypted with AES-GCM."""
    
    salt, nonce, tag = ciphertext[:16], ciphertext[16:28], ciphertext[28:44]
    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext[44:]) + decryptor.finalize()

