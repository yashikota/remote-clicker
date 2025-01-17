import socket
import pyautogui

SERVER_IP = "192.168.1.2"
SERVER_PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print("Connected to server")

try:
    while True:
        message = client.recv(1024).decode()
        if message == "CLICK":
            pyautogui.click()
            print("Clicked!")
except KeyboardInterrupt:
    print("Client shutting down.")
finally:
    client.close()
