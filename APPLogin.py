import os
import subprocess
import pyautogui
import time
from PIL import ImageGrab
from functools import partial


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


start = subprocess.Popen(['C:/Users/admin/AppData/Local/WorksMobile/NaverWorks/NaverWorks.exe'],stdout =subprocess.PIPE, shell=True)

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

i= pyautogui.locateCenterOnScreen(resource_path('ID.PNG'))
print(i)
while i is None:
 time.sleep(3)
 i= pyautogui.locateCenterOnScreen(resource_path('ID.PNG'))
 print(i)

pyautogui.click(i)
pyautogui.typewrite("*******")
print("1")

p= pyautogui.locateCenterOnScreen(resource_path('PW.PNG'))
pyautogui.click(p)
pyautogui.typewrite("*********")
print("2")

L= pyautogui.locateCenterOnScreen(resource_path('LOGON.PNG'))
pyautogui.click(L)
print("3")