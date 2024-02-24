from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# create new Firefox driver and retreive login site
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# navigate to home page
driver.get('https://www.riverblufflandscaping.com/')
time.sleep(2)

# click to blog
to_blog = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Blog")))
to_blog.click()
time.sleep(2)

# click to latest blog post
blog_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "i6wKmL")))
driver.execute_script("arguments[0].click();", blog_link)
time.sleep(2)

# close driver
driver.close()
