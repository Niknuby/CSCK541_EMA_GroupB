# CSCK541_EMA_GroupB
 To build a simple client/server network

Our code was designed to communicate with a sever through socket connection, receive encrypted data, decrypt the data, deserialise it based on the method used and saves the content received to a file.

USAGE 

## server configuration

- Confirm that the sever is running and listening for connections
- It uses Tkinter to develop the application with a graphical user interface (GUI).
- Transccribe the server's host and port configurations

### (Lines 1-9) 
Similar to the client file, the server-side code must begin by importing all the necessary code to function. It also connects to the configuration file.
### (Lines 11-25) 
In the same way that lines 7-40 on the client.py break down the code for the server to understand, these lines in server.py rebuild the code into their original formats [e.g., return] so that it’s reinstated to its former style. Additionally, for the benefit of clients, it also creates an error message on line 23.
### (Lines 25-54) 
Now that the code has been rebuilt in lines 11-24, this portion of the code is ultimately designed to speak back to the client server and deliver a set of commands, acknowledgments, and more. This code starts by connecting to the socket of the client on line 33. From here, we can see the code has a series of actions and potential dialogues with the client, the dialogues illustrated by the use of quotation marks.
### (Lines 35-36) 
If the server detects no data, the client will be shown “No data received from client.”
### (Lines 39-41) 
If the data the client inserted is not in the 3 elected languages (JSON, pickle, XML), the client will be shown “Invalid format, please choose…”
And so on…
### (Lines 56-76) 
At last, the final function of this code is to create a socket just as we did in the client function. This connects the potential socket to a potential port and IP address (line 61), and commands the code to listen out for signals from the client portal (on line 67).


 ## client configuration
 
- Modify the port and host variables in the "client.py" to match the server's port and host.
- Adjust key variables in the script with suitable key encryption

- Open terminal and select directory containing "client.py"
- Run "python client.py"

- Follow command prompt and enter ('json', 'xml', 'binary'). #serilisationmethod
- save the received content

### (Lines 1-4) 
First, the code begins by importing the necessary libraries (lines 1-4), ensuring that the Python language is recognised, but also that the formats we are choosing to speak in, such as JSON, pickle, etc., are also understood.
### (Line 5) 
Then, we attach the code to a common language understood by both the server and client-side formats (line 5) by connecting to the config file - this one line is essential to establishing a network connection.
### (Lines 7-39) 
This is an essential snippet of code and performs the "convert" function as described in the introduction of 2.2. In short, the code that you are seeing here converts JSON, Pickle, and XML into formats that can be packaged and sent to the server. JSON (lines 11-12) into a JSON string, Pickle (lines 13-14) into a byte stream, and so on.
### (Lines 40-78) 
Is the docket which is the essential connection between the client side and the server side. This code contains 5 essential commands to connect to the servers: 1 (line 44) connect to the server, which establishes the end location of the data, 2 (line 48) allow the user to choose the serial format, which is essentially asking the user to choose the language or packaging style they wish for the data to be transmitted, 3 (line 54) asking the user to log their information, 4 and 5 (packing and hitting send on the data).


## reception and decryption

- The cryptography library's Fernet symmetric encryption technique is used in both scripts for data encryption and decryption. 
- The program's general flow is coordinated by the main function.
- Once the script has established a connection with the server it will receive encrypted data
- By using the encryption key the data can now be decrypted
- Dependent on the serilisation method chosen the data will then deserialise
- Data is then saved to file

## Testing
- Written unit tests for the following is located under the 'tests' folder: 
  - client
  - server
  - serialisation
  - encryption