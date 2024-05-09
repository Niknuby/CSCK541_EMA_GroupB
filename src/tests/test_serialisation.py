import unittest
from common.serialisation import serialise_data, deserialise_data

class TestSerialisation(unittest.TestCase):
    
    def setUp(self):
        self.data = {
            'name': 'Alice',
            'age': 25,
            'is_active': True,
            'scores': [85, 90, 95]
        }

    def test_json_serialisation(self):
        
        serialised = serialise_data(self.data, 'json')
        deserialised = deserialise_data(serialised, 'json')
        self.assertEqual(self.data, deserialised)

    def test_pickle_serialisation(self):
        
        serialised = serialise_data(self.data, 'pickle')
        deserialised = deserialise_data(serialised, 'pickle')
        self.assertEqual(self.data, deserialised)

    def test_xml_serialisation(self):
        
        serialised = serialise_data(self.data, 'xml')
        deserialised = deserialise_data(serialised, 'xml')
        self.assertEqual(self.data, deserialised)

if __name__ == '__main__':
    unittest.main()
