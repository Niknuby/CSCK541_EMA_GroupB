import unittest
from client.client import serialise_data

class TestClient(unittest.TestCase):
    
    def test_serialize_data(self):
        data = {
            'name': 'Alice',
            'age': 25,
            'is_active': True
        }
        serialized = serialise_data(data, 'json')
        self.assertTrue(serialised.startswith(b'{'))

if __name__ == '__main__':
    unittest.main()
