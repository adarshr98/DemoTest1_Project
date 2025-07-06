import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

student_name = "student"
student_password = "Password123"

driver.find_element(By.ID,"username").send_keys(student_name)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys(student_password)
driver.find_element(By.CSS_SELECTOR,".btn").click()

wait = WebDriverWait(driver,10)
login_Msg = wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME,"h1"))).text
print(login_Msg)

driver.get("https://practicetestautomation.com/practice/")

driver.find_element(By.LINK_TEXT,"Test Exceptions").click()
driver.find_element(By.XPATH,"//button[@name='Add']").click()
wait = WebDriverWait(driver,10)
New_Item = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div[id='row2'] input[type='text']")))
New_Item.send_keys("Burger")
driver.find_element(By.XPATH,"//div[@id='row2']//button[1][@class='btn']").click() #To get 3rd child and 1st button under a div
driver.find_element(By.XPATH,"//div[@id='row2']//button[text()='Edit']").click()

action = ActionChains(driver)
clear_content = driver.find_element(By.CSS_SELECTOR,"div[id='row2'] input[type='text']")
action.move_to_element(clear_content).perform()
clear_content.clear()

New_item2 = "Biriyani"
driver.find_element(By.CSS_SELECTOR,"div[id='row2'] input[type='text']").send_keys(New_item2)
driver.find_element(By.CSS_SELECTOR,"div[id='row2'] > button:nth-of-type(1)").click()
Ttile_page = driver.find_element(By.CSS_SELECTOR,"div.max-width h2").text
print(Ttile_page)


time.sleep(4)