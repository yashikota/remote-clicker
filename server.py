from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

connected_clients = {}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    client_id = request.sid
    connected_clients[client_id] = True
    print(f"Client connected: {client_id}")
    emit("server_response", {"status": f"Client connected: {client_id}"}, to=client_id)

@socketio.on("disconnect")
def handle_disconnect():
    client_id = request.sid
    if client_id in connected_clients:
        del connected_clients[client_id]
    print(f"Client disconnected: {client_id}")

@socketio.on("click_signal")
def handle_click_signal():
    client_id = request.sid
    if client_id in connected_clients:
        emit("server_response", {"status": "Click signal received!"}, to=client_id)
        print("Click signal sent to client.")
    else:
        emit("server_response", {"status": "No client connected!"}, to=client_id)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
