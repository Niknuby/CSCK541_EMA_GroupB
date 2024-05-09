import unittest
from server.server import deserialise_data

class TestServer(unittest.TestCase):
    
    def test_deserialize_data(self):
        data = '{"name": "Alice", "age": 25, "is_active": true}'
        deserialized = deserialise_data(data.encode('utf-8'), 'json')
        self.assertEqual(deserialised['name'], 'Alice')

if __name__ == '__main__':
    unittest.main()
