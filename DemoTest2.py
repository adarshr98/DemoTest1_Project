import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://automationexercise.com")
expectecd_list = ['Blue Top', 'Men Tshirt']
actual_list = []

#click sigup/sign
driver.find_element(By.LINK_TEXT,"Signup / Login").click()
#enter credentials and login
email = "user2@phptravels.com"
password = "Akash@99"
driver.find_element(By.XPATH,"//form[@action='/login']//input[@type='email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"form[action='/login'] input[type='password']").send_keys(password)
driver.find_element(By.CSS_SELECTOR,"div[class='row'] > div:nth-child(1) form button").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='single-products']")))
total_products = driver.find_elements(By.XPATH,"//div[@class='single-products']")

action = ActionChains(driver)
for i in range(len(total_products)):
    try:
        products = driver.find_elements(By.XPATH,"//div[@class='single-products']")
        product = products[i]
        product_name = product.find_element(By.CSS_SELECTOR, ".productinfo > p").text.strip()
        actual_list.append(product_name)
    except StaleElementReferenceException:
        print("Element not found")
    #we are not using actionchains for text is because, even though sliding product page covers the main product page,
    #text's can be extracted but for clicks, action chains should be used

    if product_name in ['Blue Top', 'Men Tshirt']:
        action.move_to_element(product).perform()
        #evem though it is stored in a variable called product_name, actionchain expects a webelement and hence we have to,
        #use action.move_to_element(product) instead of action.move_to_element(product_name), because product_name is in string format
        wait = WebDriverWait(driver,10)
        product_list = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,".//a")))
        product_list.click()

driver.find_element(By.CSS_SELECTOR,"div.shop-menu > ul.nav > li:nth-of-type(3) > a").click()
try:
    driver.find_element(By.CSS_SELECTOR,"a.btn.btn-default.check_out").click()
except Exception as e:
    print("Click failed, but page might have changed:", e)
Overall_Total = driver.find_elements(By.XPATH,"//tr/td[5]/p")

sum = 0
for Total in Overall_Total:
    final_Total = Total.text.strip()
    final_Total = ''.join(filter(str.isdigit, final_Total))
    sum = sum + int(final_Total)

print("Total is:", sum)
click_button = driver.find_element(By.XPATH,"//div[@class='container']/div/a")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
click_button.click()
#This is javascript executor, this is used if we get the error called: ElementNotInteractableException, ElementClickInterceptedException
#And also if the element is not viewable, we may receive any error, in that case, javascript executor shoudld be used
#(0,document.body.scrollHeight);") - This allow us to scroll from top to bottom

#carddetails
driver.find_element(By.XPATH,"//div[@class='col-md-4']/form/div[1]/div/input").send_keys("1234")
driver.find_element(By.CSS_SELECTOR,"div.col-md-4 form div:nth-of-type(2) div input.form-control.card-number").send_keys("34567")
driver.find_element(By.XPATH,"//div[@class='col-md-4']/form/div[3]/div/input[@name='cvc']").send_keys("123")
driver.find_element(By.CSS_SELECTOR,"div.col-md-4 form div:nth-of-type(3) div:nth-child(2) input[name='expiry_month']").send_keys("234")
driver.find_element(By.XPATH,"//div[@class='col-md-4']/form/div[3]/div[3]/input[@name='expiry_year']").send_keys("2001")
driver.find_element(By.ID,"submit").click()
FinalMsg = driver.find_element(By.XPATH,"//div[@class='col-sm-9 col-sm-offset-1']/p[text()='Congratulations! Your order has been confirmed!']")
Success = FinalMsg.text
print(Success)


time.sleep(3)

#Explanation of the code: the DOM frequently changes and hence the explanation
#1) Here we have used len, i - because in the current ur;, the DOM get's changed frewuently, so what happens is that,
#it re-orders the products, sometimes, it may not load the full products, it may not fetch full products
#2) eg: total_products = driver.find_elements(By.XPATH,"//div[@class='single-products']") - in this, we have fetched the complete
#products list but again in the for loop we have fetched again
#like this- for i in range(len(total_products)):
    # products = driver.find_elements(By.XPATH,"//div[@class='single-products']")
    # product = products[i]
#3) we are fetching the details again bcoz, from time to time the DOM is changing, and hence we are re-fetching the getting the
#details again and getting the product count in the form of "len" and storing it in index "i"
#4) Usually we won't perform using "len", index "i" to get the products, this is because the DOM of HTML is getting changed here