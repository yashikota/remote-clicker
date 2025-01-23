import pyautogui
from flask import Flask

app = Flask(__name__)


@app.route("/click")
def click():
    try:
        pyautogui.click()
        print("Clicked!")
        return "Clicked!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
