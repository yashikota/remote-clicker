import requests

clients = [
    {"url": "http://192.168.10.20:8888/click"},
]

def send_click(client):
    try:
        response = requests.get(client["url"], timeout=3)
        print(f"Response from {client['url']}: {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

try:
    while True:
        input("Press Enter to send click... (Ctrl+C to exit)")
        for client in clients:
            send_click(client)
except KeyboardInterrupt:
    print("\nProgram terminated by user")
