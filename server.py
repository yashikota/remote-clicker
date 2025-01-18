from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socket

app = Flask(__name__)
socketio = SocketIO(app)

HOST = "0.0.0.0"
PORT = 12345
conn = None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("click_signal")
def handle_click_signal():
    global conn
    if conn:
        conn.send(b"CLICK")
        print("Click signal sent to client.")
        emit("server_response", {"status": "Click signal sent!"})
    else:
        emit("server_response", {"status": "No client connected!"})

@socketio.on("connect_client")
def connect_client():
    global conn
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    emit("server_response", {"status": f"Client connected: {addr}"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
