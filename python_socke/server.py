import socket
import json
import xml.etree.ElementTree as ET
import base64
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip

# Initialize Socket Instance
sock = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

print('The key is :', key)

# Binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')


def select_file():
    global filename
    filename = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)


def select_serialization():
    global serialization_method
    serialization_method = serialization_var.get()


def copy_key():
    pyperclip.copy(key.decode())
    messagebox.showinfo("Key Copied", "The key has been copied to the clipboard.")


def transfer_file():
    global filename, serialization_method
    serialization_method = serialization_var.get()  # Declare global variables
    if not filename:
        messagebox.showerror("Error", "Please select a file to transfer!")
        return

    # Read File
    try:
        with open(filename, 'rb') as file:
            content = file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
        return

    if serialization_method == "json":
        # Base64 encode the content for JSON serialization
        content_base64 = base64.b64encode(content).decode()
        serialized_data = json.dumps({"file_content": content_base64}).encode()
    elif serialization_method == "xml":
        # Serialize using XML
        root = ET.Element("data")
        ET.SubElement(root, "file_content").text = content.decode()
        serialized_data = ET.tostring(root)
    else:
        # Serialize using pickle (binary)
        serialized_data = content

    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(serialized_data)

    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Send the encrypted data to the client
    con.send(encrypted_data)

    print('File has been transferred successfully.')

    con.close()


# Initialize the Tkinter window
window = tk.Tk()
window.title("Secure File Transfer")

# Create labels and entry for filename
filename_label = tk.Label(window, text="File to Send:")
filename_label.pack()
filename = ""
file_entry = tk.Entry(window, width=50)
file_entry.pack()
select_file_button = tk.Button(window, text="Browse", command=select_file)
select_file_button.pack()

# Create radio buttons for serialization method
serialization_var = tk.StringVar()
serialization_var.set("json")  # Set default selection

json_radio = tk.Radiobutton(window, text="JSON", variable=serialization_var, value="json", command=select_serialization)
json_radio.pack()
xml_radio = tk.Radiobutton(window, text="XML", variable=serialization_var, value="xml", command=select_serialization)
xml_radio.pack()
binary_radio = tk.Radiobutton(window, text="Binary", variable=serialization_var, value="binary", command=select_serialization)
binary_radio.pack()

# Label to display the generated key
key_label = tk.Label(window, text="Generated Key: " + key.decode())
key_label.pack()

# Button to copy the key
copy_button = tk.Button(window, text="Copy Key", command=copy_key)
copy_button.pack()

# Create a button to initiate transfer
transfer_button = tk.Button(window, text="Transfer File", command=transfer_file)
transfer_button.pack()

# Run the main loop
window.mainloop()
