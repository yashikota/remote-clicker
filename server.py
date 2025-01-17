import socket

HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

try:
    while True:
        input("Press Enter to send a click signal...")
        conn.send(b"CLICK")
        print("Click signal sent!")
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    conn.close()
    server.close()
