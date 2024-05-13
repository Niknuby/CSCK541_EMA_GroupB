import socket
import json
import xml.etree.ElementTree as ET
import base64
from cryptography.fernet import Fernet

# Initialize Socket Instance
sock = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')

# Send a greeting to the server
sock.send('A message from the client'.encode())

# Receive the data from the server
data = sock.recv(4096)

# Decrypt the data
key = b'er0xZuGt9b4FN_LqeloPsMWs97jFlN1aX7Z0W543sts=' # Provide the key here
cipher_suite = Fernet(key)
decrypted_data = cipher_suite.decrypt(data)

# Prompt user for the serialization method used by the server
serialization_method = input("Enter the serialization method used by the server (json, xml, binary): ")

if serialization_method == "json":
    # Deserialize using JSON
    deserialized_data = json.loads(decrypted_data)
    # Base64 decode the content
    content_base64 = deserialized_data["file_content"]
    content = base64.b64decode(content_base64)
elif serialization_method == "xml":
    # Deserialize using XML
    root = ET.fromstring(decrypted_data)
    content = root.find("file_content").text.encode()
else:
    # Deserialize using pickle (binary)
    content = decrypted_data

# Prompt user for the file name to save
filename = input("Enter the name of the file to save: ")

# Write the data to a file
with open(filename, 'wb') as file:
    file.write(content)

print('File has been received and decrypted successfully.')

sock.close()
print('Connection Closed.')
