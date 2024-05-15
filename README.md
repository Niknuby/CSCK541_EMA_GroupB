# CSCK541_EMA_GroupB
 build a simple client/server network

Our code was designed to communicate with a sever through socket connection, receive encrypted dat, decrypt the data, deserialize it based on the method used and saves the content received to a file.

USAGE 

## server configuration

- Confirm that the sever is running and listening for connections
- Transccribe the server's host and port configurations

 ## client configuration
 
- Modify the port and host variables in the "client.py" to match the server's port and host.
- Adjust key variables in the script with suitable key encryption

- Open terminal and select directory containing "client.py"
- Run "python client.py"

- Follow command prompt and enter ('json', 'xml', 'binary'). #serilisationmethod
- save the received content

## reception and decryption

- Once the script has established a connection with the server it will receive encrypted data
- By using the encryption key the data can now be decrypted
- Dependent on the serilisation method chosen the data will then deserialise
- Data is then saved to file
