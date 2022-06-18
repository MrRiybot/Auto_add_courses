from add import ADD
from datetime import datetime
import time

driverpath = input(
    "Enter your driverpath (must be in the same folder) example 'Chromedriver.exe': ")
url = ""
login = ""
password = ""
driver = ADD.login(url, login, password, driverpath)
