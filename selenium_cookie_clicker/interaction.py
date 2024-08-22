from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Interact with wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # # Click the link
# # article_count.click()
#
# # Find element by Link text
# # all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value="search")
#
# # Send keyboard input - import Keys to enter
# search.send_keys("Python", Keys.ENTER)


# Use test webpage to fill out the sign-up form and submit it
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, value="fName")
last_name_field = driver.find_element(By.NAME, value="lName")
email_field = driver.find_element(By.NAME, value="email")
submit_button = driver.find_element(By.TAG_NAME, value="button")

# Fill out form and submit
first_name_field.send_keys("Name")
last_name_field.send_keys("Name")
email_field.send_keys("Name@gmail.com")

submit_button.send_keys(Keys.ENTER)


# driver.quit()
