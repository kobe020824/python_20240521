from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
import datetime
from datetime import datetime


browser = webdriver.Chrome()    #Chrome webdriver path
browser.get('http://google.com')    #web url
browser.set_window_size(860,800)       #web browser size set

# search word input_search by find_element
#element = browser.find_Element_By_XPath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# searchword box click
element.click()

# search word input
element.send_keys("서태지")

# search word process(enter)
element.send_keys(Keys.ENTER)

# Wait for () second(s)
sleep(5)

# browser.close
browser.close()
