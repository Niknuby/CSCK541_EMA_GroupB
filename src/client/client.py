import socket
import json
import pickle
import xml.etree.ElementTree as ET
from config import SERVER_ADDRESS, SERVER_PORT, BUFFER_SIZE

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
        raise ValueError("Unsupported serialization format")


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


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        print("Connected to server at {}:{}".format(SERVER_ADDRESS, SERVER_PORT))

        # Allow user to choose serialisation format
        format_type = input("Enter serialisation format (json/pickle/xml): ").strip().lower()
        while format_type not in ['json', 'pickle', 'xml']:
            print("Invalid format. Please choose 'json', 'pickle', or 'xml'.")
            format_type = input("Enter serialisation format (json/pickle/xml): ").strip().lower()

        # Example data to be sent
        data = {
            'name': 'John Doe',
            'age': 30,
            'is_active': True,
            'scores': [12, 15, 18]
        }

        # Serialise data
        serialised_data = serialise_data(data, format_type)
        client_socket.sendall(serialised_data)
        print("Data sent to server.")

        # Receive response
        received_data = client_socket.recv(BUFFER_SIZE)
        print("Received from server:", received_data.decode('utf-8'))

    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()