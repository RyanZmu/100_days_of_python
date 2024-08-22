from selenium import webdriver
from selenium.webdriver.common.by import By


# Firefox options
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

# search_box = driver.find_element(By.NAME, value="q")
# print(search_box.tag_name)
# # Get value from the element directly - accesses html/css attributes
# print(search_box.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# # Use CSS selector to find elements
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# # Use Xpath html/body/div/p/a - Right click element and copy Xpath
# bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

# Get Upcoming Events as a dict {0: {"time", "name"},}
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

# close will close tab
# driver.close()
# quit will close the entire window
driver.quit()



