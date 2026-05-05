from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


time.sleep(2)
keyboard.press(Key.space)
keyboard.release(Key.space)
