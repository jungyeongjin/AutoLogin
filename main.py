import subprocess
import time

subprocess.call("Login_Selenium.py", shell=True)
time.sleep(5)
subprocess.call("APPLogin.py", shell=True)
