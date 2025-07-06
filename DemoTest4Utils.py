from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def close_ads(driver):
    try:
        ad_button = driver.find_element(By.XPATH, "//div[contains(@class, 'sa-button-container')]//button[text()='OK']")
        ad_button.click()
        print("[INFO] Ad popup closed.")
    except:
        print("[INFO] No ad popup found or already closed.")

def safe_click(driver, element):
    try:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(element))
        element.click()
    except Exception as e:
        close_ads(driver)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        try:
            element.click()
        except Exception as ex:
            print(f"[ERROR] Still not clickable: {ex}")

def wait_and_close_ads(driver):
    for attempt in range(2):  # Try twice if needed
        try:
            ad_button = WebDriverWait(driver, 7).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'sa-button-container')]//button[text()='OK']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", ad_button)
            time.sleep(0.5)
            ad_button.click()
            print(f"[INFO] Ad closed on attempt {attempt + 1}")
            return
        except Exception as e:
            print(f"[INFO] No ad to close or not ready yet on attempt {attempt + 1}")
            time.sleep(1)



#why to use javascript executor when we have explicit waits?

# BUT — When .click() Still Fails Even After Wait
# Yes, this happens. Even if element_to_be_clickable passes, .click() might still fail if:
# Problem	Why click() still fails
# Overlays still cover the element	Wait doesn't detect that it’s blocked by another layer
# Element animates in/out	Appears clickable, but DOM state is unstable
# Custom JavaScript prevents interaction	Site’s scripts hijack clicks or use event delegation
# Element rendered inside a shadow DOM or iframe	Wait works, but .click() hits a boundary Selenium can't cross

#Basically we should try performin with explicit waits before jumping into javascript executor