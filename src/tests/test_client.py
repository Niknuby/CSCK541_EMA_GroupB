import unittest
from client.client import serialise_data

class TestClient(unittest.TestCase):
    
    def test_serialise_data(self):
        data = {
            'name': 'Alice',
            'age': 25,
            'is_active': True
        }
        serialised = serialise_data(data, 'json')
        self.assertTrue(serialised.startswith(b'{'))

if __name__ == '__main__':
    unittest.main()
