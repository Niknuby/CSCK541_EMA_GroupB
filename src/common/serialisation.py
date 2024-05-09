import json
import pickle
import xml.etree.ElementTree as ET

def serialise_data(data, format_type):
    
    """ Serialise data into specified format: 'json', 'pickle', or 'xml' """
    
    if format_type == 'json':
        return json.dumps(data).encode('utf-8')
    elif format_type == 'pickle':
        return pickle.dumps(data)
    elif format_type == 'xml':
        root = ET.Element("data")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return ET.tostring(root)
    else:
        raise ValueError("Unsupported serialisation format")

def deserialise_data(data, format_type):
    
    """ Deserialise data from specified format """
    
    if format_type == 'json':
        return json.loads(data)
    elif format_type == 'pickle':
        return pickle.loads(data)
    elif format_type == 'xml':
        root = ET.fromstring(data)
        return {child.tag: child.text for child in root}
    else:
        raise ValueError("Unsupported serialisation format")
