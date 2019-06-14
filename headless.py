# Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException        
import time
import json

# Set the url
url = "https://analytics.google.com/analytics/web/?authuser=1#/a69568077w106628147p111548331/admin/trackingreferral-exclusion-list/"

# Get configuration
with open("config.json", 'r') as f:
	config = json.load(f)

# Get login credentials
with open("login_credentials.json", 'r') as f:
	login = json.load(f)

# Run Headless Chrome
options = Options()  
options.headless = False
driver = webdriver.Chrome('./chromedriver', chrome_options=options)  

# Open web page
driver.implicitly_wait(30)
driver.get(url)

# Return page source
print("Page loaded: {}".format(driver.current_url))


# Login
print("+++++ Authentication +++++")
time.sleep(1)
driver.execute_script("arguments[0].value='{}'".format(login['username']), driver.find_element_by_css_selector(config['loginInput']))
print("Entered username")

time.sleep(1)
driver.find_element_by_css_selector(config['loginNext']).click()
print("DOM element loginNext clicked")

time.sleep(3)
driver.execute_script("arguments[0].value='{}'".format(login['password']), driver.find_element_by_css_selector(config['loginInput']))
print("Entered password")

time.sleep(1)
driver.find_element_by_css_selector(config['passwordNext']).click()
print("DOM element passwordNext clicked")

# Find out if we are logged in
time.sleep(15)
try:
    driver.find_element_by_css_selector(config['GABody'])
    print("Login successful")
    print("\n+++++ Analytics tasks +++++")
    print("Page loaded: {}".format(driver.current_url))

except NoSuchElementException:
    print("Login failed. Try again.")

# Add Referral Exclusion
time.sleep(5)
print("Attempt to click AddReferralExclusion")
driver.find_element_by_css_selector(config['AddReferralExclusion']).click()
print("DOM element AddReferralExclusion clicked")







