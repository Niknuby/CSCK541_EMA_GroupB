from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("Generated Key:", key.decode())