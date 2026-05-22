from pynput.mouse import Button ,Controller
import subprocess
import time


mouse = Controller()

subprocess.call("C:\\Program Files (x86)\\Razer\\Razer Cortex\\CortexLauncher.exe")

time.sleep(1)

mouse.position = (278, 63)
mouse.click(Button.left,1)
