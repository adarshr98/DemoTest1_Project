import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver import ActionChains

from pythonTestcase1.DemoTest4Utils import close_ads, wait_and_close_ads, safe_click

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://magento.softwaretestingboard.com/")
time.sleep(2)

wait_and_close_ads(driver)

# Hover to Men > Tops > Jackets
action = ActionChains(driver)
#driver.execute_script("window.scrollBy(0, 300);")

MenProduct = driver.find_element(By.ID, "ui-id-5")
action.move_to_element(MenProduct).pause(1).perform()

MenTop = driver.find_element(By.ID, "ui-id-17")
action.move_to_element(MenTop).pause(1).perform()

# Wait and click Jackets
MenJack = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.ID, "ui-id-19"))
)

# Use JavaScript to click (fallback if .click() fails)
try:
    driver.execute_script("arguments[0].click();", MenJack)
    print("[SUCCESS] Clicked Jackets using JavaScript.")
except Exception as e:
    print(f"[ERROR] Failed to click Jackets: {e}")

wait_and_close_ads(driver)

# action.move_to_element(MenJack).click().perform()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='product-item-info']")))
wait_and_close_ads(driver)
driver.save_screenshot("after_jackets_click.png")

products = driver.find_elements(By.XPATH,"//div[@class='product-item-info']")
actual_list = ['Mars HeatTech™ Pullover', 'Taurus Elements Shell']
expected_list = []

while len(expected_list) < len(actual_list):
    products = driver.find_elements(By.XPATH, "//div[@class='product-item-info']")

    for product in products:
        prod_name = product.find_element(By.XPATH, ".//a[contains(@class, 'product-item-link')]").text
        expected_list.append(prod_name)

        if prod_name in actual_list:
             prod_name_list = product.find_element(By.CSS_SELECTOR, "button[title='Add to Cart']")
             driver.execute_script("window.scrollBy(0, 500);", prod_name_list)
             action.move_to_element(prod_name_list).click().perform()

             time.sleep(1)
             wait_and_close_ads(driver)

             wait = WebDriverWait(driver,10)
             prod_text_name = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-title")))
             #driver.execute_script("window.scrollBy(0, 500);")
             wait_and_close_ads(driver)

             size = driver.find_element(By.ID,"option-label-size-143-item-166")
             colour = driver.find_element(By.ID,"option-label-color-93-item-49")
             time.sleep(1)
             wait = WebDriverWait(driver,10)
             Add_to_cart = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"div.actions > button.action.primary.tocart")))
             #Add_to_cart = driver.find_element(By.CSS_SELECTOR,"div.actions > button.action.primary.tocart")
             driver.execute_script("window.scrollBy(0, 800);")
             size.click()
             colour.click()
             Add_to_cart.click()
             print(prod_text_name)


time.sleep(10)






#When interviewer asks how to handle ad's?
# Sample Interview Answer
# “When I encounter ads or modal popups during Selenium automation, I handle them proactively to ensure they don’t interfere with the test flow. Here's how I manage them:
#
# Wait briefly after page load using time.sleep() or WebDriverWait to give the ad time to appear.
#
# Detect if a popup exists using XPath with flexible matching (e.g., contains(text(),'×'), aria-label='close', or class attributes like close, dismiss, etc.).
#
# Use is_displayed() or try-catch logic to confirm visibility.
#
# Dismiss the ad using .click() or driver.execute_script("arguments[0].click()", element) in case the element is overlayed or not directly clickable.
#
# I put this logic inside a reusable method like close_ads(driver) and call it in test scripts before continuing with menu navigation or actions.

# ------------------------------------

# Bonus: Key Terms to Mention
# If you want to impress the interviewer, sprinkle in these:
#
# Exception Handling: try-except for NoSuchElementException or ElementNotInteractableException
#
# Dynamic XPath: Using contains() and translate() to match lowercase versions of class names
#
# JavaScript Click Fallback: driver.execute_script(...) when normal .click() fails
#
# Reusability: Utility method like close_ads(driver) to keep code modular
#
# Screenshots: Saving screenshots for debugging (e.g., driver.save_screenshot())
#
# Optional Realistic Additions:
# You can also say:
#
# "In some cases, ads are rendered inside iframes, so I check driver.switch_to.frame() if I can’t interact with them normally.

