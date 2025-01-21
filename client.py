from websocket import create_connection, enableTrace
import pyautogui
import json

enableTrace(True)
SERVER_URL = "ws://150.89.229.144:5000/socket.io/?EIO=4&transport=websocket"

try:
    ws = create_connection(SERVER_URL)
    print("Connected to server")

    while True:
        response = ws.recv()

        try:
            data = json.loads(response)
            if data.get("type") == "event" and data.get("name") == "click_signal":
                pyautogui.click()
                print("Clicked!")
        except json.JSONDecodeError:
            pass

except KeyboardInterrupt:
    print("Client shutting down.")
finally:
    ws.close()
