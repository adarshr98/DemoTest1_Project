import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.demoblaze.com/")

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']//a[@class='hrefch']")
actual_phonelist = ['Samsung galaxy s6', 'Nokia lumia 1520']
expectecd_phonelist = []

# Loop until we add all desired phones
while len(expectecd_phonelist) < len(actual_phonelist):
#while loop explanantion - “Is the number of phones already added less than the total number you want?”
#If yes, it continues, and if no, it stops

     #Refresh product list each time
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']//a[@class='hrefch']")
    for i in range(len(products)):
        # Re-locate product list
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']//a[@class='hrefch']")
        name = products[i].text

        if name in actual_phonelist and name not in expectecd_phonelist:
            products[i].click()

            # Wait and click Add to cart
            WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
            ).click()

            # Handle alert
            WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
            driver.switch_to.alert.accept()
            expectecd_phonelist.append(name)

            # Go back to Home
            driver.find_element(By.XPATH, "//a[text()='Home ']").click()

            # Wait for product list to appear again
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='card h-100']//a[@class='hrefch']"))
            )
            break  # ✅ Break to refresh loop and get fresh DOM after navigating


# Proceed to cart
driver.find_element(By.LINK_TEXT, "Cart").click()
time.sleep(2)

# Click "Place Order"
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
time.sleep(2)

# Fill the form
name = "Adarsh Ravichandran"
Country = "India"
City = "Coimbatore"
Credit_card = "001"
Month = "August"
Year = "1987"

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "country").send_keys(Country)
driver.find_element(By.ID, "city").send_keys(City)
driver.find_element(By.ID, "card").send_keys(Credit_card)
driver.find_element(By.ID, "month").send_keys(Month)
driver.find_element(By.ID, "year").send_keys(Year)

# Optional: Confirm purchase
# driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

PurchaseButton = driver.find_element(By.XPATH,"//div[@class='modal-content']/div[3]/button[text()='Purchase']")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
PurchaseButton.click()

FinalMsg = driver.find_element(By.CSS_SELECTOR,"div.sweet-alert.showSweetAlert.visible > h2:nth-child(6)").text
print(FinalMsg)

driver.find_element(By.XPATH,"//div[contains(@class, 'sa-button-container')]//button[text()='OK']").click()

time.sleep(5)
driver.quit()
