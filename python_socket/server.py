import socket
import json
import xml.etree.ElementTree as ET
import base64
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip

# Initialise Socket Instance
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


def select_serialisation():
    global serialisation_method
    serialisation_method = serialisation_var.get()


def copy_key():
    pyperclip.copy(key.decode())
    messagebox.showinfo("Key Copied", "The key has been copied to the clipboard.")


def transfer_file():
    global filename, serialisation_method
    serialisation_method = serialisation_var.get()  # Declare global variables
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

    if serialisation_method == "json":
        # Base64 encode the content for JSON serialisation
        content_base64 = base64.b64encode(content).decode()
        serialised_data = json.dumps({"file_content": content_base64}).encode()
    elif serialisation_method == "xml":
        # Serialise using XML
        root = ET.Element("data")
        ET.SubElement(root, "file_content").text = content.decode()
        serialised_data = ET.tostring(root)
    else:
        # Serialise using pickle (binary)
        serialised_data = content

    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(serialised_data)

    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Send the encrypted data to the client
    con.send(encrypted_data)

    print('File has been transferred successfully.')

    con.close()


# Initialise the Tkinter window
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

# Create radio buttons for serialisation method
serialisation_var = tk.StringVar()
serialisation_var.set("json")  # Set default selection

json_radio = tk.Radiobutton(window, text="JSON", variable=serialisation_var, value="json", command=select_serialisation)
json_radio.pack()
xml_radio = tk.Radiobutton(window, text="XML", variable=serialisation_var, value="xml", command=select_serialisation)
xml_radio.pack()
binary_radio = tk.Radiobutton(window, text="Binary", variable=serialisation_var, value="binary", command=select_serialisation)
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
