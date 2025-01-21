import websocket
import json
import pyautogui

websocket.enableTrace(True)

SERVER_URL = "ws://150.89.229.144:5000/socket.io/?EIO=4&transport=websocket"

try:
    ws = websocket.create_connection(SERVER_URL)
    print("Connected to server")

    while True:
        response = ws.recv()
        print(f"Raw response: {response}")

        try:
            data = json.loads(response)

            if isinstance(data, dict) and data.get("type") == "event" and data.get("name") == "click_signal":
                pyautogui.click()
                print("Clicked!")
        except json.JSONDecodeError:
            print(f"Invalid JSON received: {response}")
        except AttributeError:
            print(f"Unexpected data structure: {response}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if "ws" in locals():
        ws.close()
        print("WebSocket connection closed.")
