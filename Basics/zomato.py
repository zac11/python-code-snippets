import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin

##### Web scrapper for infinite scrolling page #####
driver = webdriver.Chrome(executable_path=r"/Users/Rahul_Yadav/Downloads/chromedriver")

driver.get("https://www.zomato.com/pune/delivery-in-budhwar-peth")

time.sleep(10)  # Allow 2 seconds for the web page to open
driver.find_element_by_xpath("//div[contains(text(),'Rating: 4.0+')]").click()
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1
count=0

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
for img in soup.find_all('img',alt='Restaurant Card'):
    count+=1
print('Count of all rests is',count)
print("\n".join([img['alt'] for img in soup.find_all('img', alt='Restaurant Card')]))
##### Extract Reddit URLs #####
'''soup = BeautifulSoup(driver.page_source, "html.parser")
for parent in soup.find_all('img', alt='Restaurant Card'):
    print(len(parent))'''

driver.quit()