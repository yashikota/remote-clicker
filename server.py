from flask import Flask, jsonify
import requests

app = Flask(__name__)

clients = [
    {"name": "client1", "url": "http://client1_ip:8888/click"},
    {"name": "client2", "url": "http://client2_ip:8888/click"},
]

@app.route("/send_click", methods=["POST"])
def send_click():
    try:
        for client in clients:
            response = requests.post(client["url"])
            print(f"{client['name']}: {response.status_code}")
        return jsonify({"message": "Clicked!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
