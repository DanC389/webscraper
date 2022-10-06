from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/Users/danie/source/repos/WebScraper1/chromedriver_win32/chromedriver.exe')
#driver.maximize_window() # For maximizing window
driver.implicitly_wait(15) # gives an implicit wait for 10 seconds

driver.get('https://www.namus.gov/Dashboard?nocache=')

players = driver.find_elements("xpath", '//div[@class="ui-grid-cell-contents"]')

num2 = 0
num = 0
players_list = []

for p in range(len(players)):
    num = num + 1
    players_list.append(players[p].text)
    print(players_list[p])

    # new line after 9 subset of data per row
    if num % 9 == 0:
        print("\n")
        num2 = num2 + 1

# number of data sets
print(num2)

   # requests.get
