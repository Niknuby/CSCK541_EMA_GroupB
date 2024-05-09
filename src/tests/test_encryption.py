# test_encryption.py

import unittest
from common.encryption import encrypt_data, decrypt_data

class TestEncryption(unittest.TestCase):
    
    def setUp(self):
        self.data = b"Sensitive data that needs encryption"
        self.password = "securepassword"

    def test_encryption_decryption(self):
        
        encrypted_data = encrypt_data(self.data, self.password)
        decrypted_data = decrypt_data(encrypted_data, self.password)
        self.assertEqual(self.data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
