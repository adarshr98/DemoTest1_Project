import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from pageObjects.FoodPage import FoodPage
from pageObjects.PractiseTestPage import PractiseTestPage
from pageObjects.login import LoginPage
from pageObjects.loginConfirmPage import LoginConfirmPage

test_data_path = "../data/test_DemoTest.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("test_list_item", test_list)
def test_DemoTest1(browserInstance, test_list_item):
    driver=browserInstance
    loginPage = LoginPage(driver)
    loginPage.login_Page(test_list_item['student_name'], test_list_item['student_password'])
    print(loginPage.getTitle())
    loginConfirmPage = LoginConfirmPage(driver)
    loginConfirmPage.login_confirm_page()
    print(loginConfirmPage.getTitle())
    practiseTestUrl = PractiseTestPage(driver)
    practiseTestUrl.practise_Test_Url(test_list_item['practise_url'])
    print(practiseTestUrl.getTitle())
    TestExceptionclick = PractiseTestPage(driver)
    TestExceptionclick.Test_Exception_click()
    foodPage = FoodPage(driver)
    foodPage.scroll_by_view()
    foodPage.add_item()
    foodPage.save_button()
    foodPage.edit_button()
    foodPage.clear_item1_and_add_item2()
    print(foodPage.getTitle())



    # driver.execute_script("window.scrollBy(0, 500);")
    # driver.find_element(By.XPATH,"//button[@name='Add']").click()
    # wait = WebDriverWait(driver,10)
    # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div[id='row2'] > input.input-field")))
    #
    # Item1 = "Burger"
    # driver.find_element(By.CSS_SELECTOR,"div[id='row2'] > input.input-field").send_keys(Item1)
    #
    # #savebutton
    # driver.find_element(By.XPATH, "//div[@id='row2']//button[1][@class='btn']").click()
    #
    # #edit button
    # driver.find_element(By.XPATH,"//div[@id='row2']/button[@id='edit_btn']").click()
    #
    # wait = WebDriverWait(driver,10)
    # clearContent = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"div[id='row2'] > input[type='text']")))
    #
    # action = ActionChains(driver)
    # action.move_to_element(clearContent).click().perform()
    #
    # clearContent.clear()
    #
    # clearContent.send_keys("Biriyani")
    # driver.find_element(By.CSS_SELECTOR,"div[id='row2'] > button:nth-child(3)").click()




    time.sleep(4)
