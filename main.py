from add import ADD
from add1 import ADD as ADD2
from datetime import datetime
import time

driverpath = input(
    "Enter your driverpath (must be in the same folder) example 'Chromedriver.exe': ")
choice = input("did you have any current courses in your term? (yes/no):")
if(choice == "yes"):
    driver = ADD2.login('', '', '', driverpath)
else:
    driver = ADD.login('', '', '', driverpath)
