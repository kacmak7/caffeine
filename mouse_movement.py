import pyautogui as mouse
import time

i=0
while True:
    time.sleep(240) # 4 minutes
    x, y = mouse.position()
    i += 1
    if(i % 2 == 0):
        mouse.moveTo(x+1, y+1)
    else:
        mouse.moveTo(x-1, y-1)