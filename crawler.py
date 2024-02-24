from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# create new Firefox driver
fireFoxOptions = Options()
fireFoxOptions.add_argument("--headless")
driver = webdriver.Firefox(options=fireFoxOptions, service=
    Service(GeckoDriverManager().install()))

# navigate to home page
driver.get('https://www.riverblufflandscaping.com/')

# click to blog
to_blog = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Blog")))
to_blog.click()

# click to latest blog post
blog_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "i6wKmL")))
driver.execute_script("arguments[0].click();", blog_link)

# close driver
driver.close()