import socket
import json
import pickle
import xml.etree.ElementTree as ET
import logging
from config import SERVER_ADDRESS, SERVER_PORT, BUFFER_SIZE, LOG_FILE, LOG_FORMAT, LOG_LEVEL

# Configure logging
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=getattr(logging, LOG_LEVEL.upper()))

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

def handle_client(client_socket, address):
    
    """ Handle incoming client connections and data """
    
    logging.info(f"Connected to client at {address}")

    try:
        # Receive data
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            logging.warning(f"No data received from client {address}")
            return

        # Detect serialisation format
        format_type = input("Enter serialisation format (json/pickle/xml): ").strip().lower()
        while format_type not in ['json', 'pickle', 'xml']:
            print("Invalid format. Please choose 'json', 'pickle', or 'xml'.")
            format_type = input("Enter serialisation format (json/pickle/xml): ").strip().lower()

        # Deserialise data
        deserialised_data = deserialise_data(data, format_type)
        logging.info(f"Received data from {address}: {deserialised_data}")

        # Send acknowledgment to client
        client_socket.sendall(b"Data received successfully")
    except Exception as e:
        logging.error(f"Error processing client {address}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed for client {address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the server to the specified address and port
        server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
        server_socket.listen(5)  # Accept up to 5 concurrent connections
        logging.info(f"Server listening at {SERVER_ADDRESS}:{SERVER_PORT}")

        while True:
            client_socket, address = server_socket.accept()
            handle_client(client_socket, address)

    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        server_socket.close()
        logging.info("Server shutdown")

if __name__ == "__main__":
    main()
