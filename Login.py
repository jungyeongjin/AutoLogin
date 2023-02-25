import pywinauto
from pywinauto.application import Application
from pywinauto import findwindows
from time import sleep

app = Application(backend="uia").start(r'C:\Users\admin\AppData\Local\WorksMobile\NaverWorks\NaverWorks.exe')
sleep(3)

procs = findwindows.find_elements()

""" for proc in procs:
    print(f"{proc} / 프로세스 : {proc.process_id}") """

app.connect(title_re='NAVER WORKS' )

dig = app['NAVER WORKS' ]

#dig['Pane'].type_keys("Hello")
#dig.Custom.type_keys('Hello',with_spaces=True)
dig.print_control_identifiers()