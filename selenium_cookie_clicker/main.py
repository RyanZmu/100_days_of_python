"""
Create a bot to play Cookie Clicker for us and buy upgrades as needed
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# First page is the language selection - select English button; wait 5 seconds for popup to load fully
time.sleep(5)
language_button = driver.find_element(By.ID, value="langSelect-EN")
language_button.click()

# There is a loader div that needs to be clicked to clear it
loader_overlay = driver.find_element(By.ID, value="loader")
loader_overlay.click()

# Close cookie banner at bottom of window
banner = driver.find_element(By.XPATH, value="/html/body/div[1]/div/a[1]")
banner.click()

# Main cookie button
cookie_button = driver.find_element(By.CSS_SELECTOR, value="#cookieAnchor button")


def check_upgrade():
    # Get upgrade and costs html elements
    unlocked_upgrades_elements = driver.find_elements(By.CLASS_NAME, value="product.unlocked.enabled")
    unlocked_costs_elements = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled span")

    # Create lists for upgrades and costs
    upgrades = [upgrade.text for upgrade in unlocked_upgrades_elements]
    costs = [cost.text for cost in unlocked_costs_elements if cost.text != ""]
    print(upgrades)
    print(costs)

    # Will buy the last item of the costs array each time, usually this is the most expensive
    try:
        unlocked_upgrades_elements[len(costs) - 1].click()
    except IndexError:
        print("No upgrades available yet")
    else:
        print(f"Upgrade {unlocked_upgrades_elements[len(costs) - 1].text} bought")


timeout = time.time() + 5  # five seconds from now
five_mins = time.time() + 60*5  # five mins

while time.time() < five_mins:
    # Click cookie
    cookie_button.click()

    # Roughly every 5 seconds check for upgrade
    if time.time() > timeout:
        # Check Upgrades
        check_upgrade()

        # Add another 5 seconds to the timeout
        timeout = time.time() + 5
