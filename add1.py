from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options

class ADD:

    def login(url, id, password, driverpath):

        driver = webdriver.Chrome(executable_path=('./' + driverpath))
        driver.get("https://edugate.ksu.edu.sa/ksu/init")
        time.sleep(5)
        sections = list()
        number_of_sections = int(input("how many sections that you want to try to add?: "))
        for i in range(number_of_sections):
            section = input('section number {0}:'.format(i))
            sections.append(section)
        state = True
        while state:
            for s in sections:
                action = driver.find_element_by_id('saveBut1')
                action.click()
                time.sleep(1)
                action = driver.find_element_by_xpath('//*[@id="addSection0"]')
                action.send_keys(s)
                action = driver.find_element_by_xpath('//*[@id="left"]/div[3]/form/table[5]/tbody/tr[2]/td/table/tbody/tr/td[4]/a')
                action.click()
                time.sleep(2)
            try:
                action = driver.find_element_by_xpath('//*[@id="successAddDiv"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')
                action.click()
                for i in range(5):
                    state = False
            except:
                time.sleep(1)
                action = driver.find_element_by_xpath('//*[@id="errorAddDiv"]/table/tbody/tr[1]/td/table/tbody/tr/td/a')
                action.click()
        return driver
