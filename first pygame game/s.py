import time

from pynput.keyboard import Controller, Key

keyboard = Controller()


time.sleep(2)
keyboard.press(Key.space)
keyboard.release(Key.space)
