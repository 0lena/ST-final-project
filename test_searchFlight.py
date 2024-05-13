import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def test_valid_one_way_flight_search():
    driver.get("https://www.expedia.ca/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[contains(.,'Flights')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@id='search_form_product_selector_flights']/div/div/div/ul/li[2]/a/span").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='cabin_class']/span").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div/div/div/div/div/div[2]/div/button").click()
    leaving_from = driver.find_element(By.XPATH, "//div[@id='origin_select-menu']/section/div/div/div/input")
    leaving_from.send_keys("Toronto")
    leaving_from.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH,
                        "//div[@id='FlightSearchForm_ONE_WAY']/div/div/div/div[2]/div/div/div[2]/div/button").click()
    going_to = driver.find_element(By.XPATH, "//div[@id='destination_select-menu']/section/div/div/div/input")
    going_to.send_keys("Montreal")
    going_to.send_keys(Keys.ENTER)
    time.sleep(5)

    driver.find_element(By.ID, "search_button").click()
    time.sleep(60)
    success_search = driver.find_element(By.XPATH,
                                "//h5[normalize-space()='Recommended departing flights']").text
    assert "Recommended departing flights" == success_search, "test failed"

def test_invalid_destination_one_way_flight_search():
    driver.get("https://www.expedia.ca/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[contains(.,'Flights')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@id='search_form_product_selector_flights']/div/div/div/ul/li[2]/a/span").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='cabin_class']/span").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ONE_WAY']/div/div/div/div/div/div/div[2]/div/button").click()
    leaving_from = driver.find_element(By.XPATH, "//div[@id='origin_select-menu']/section/div/div/div/input")
    leaving_from.send_keys("")
    leaving_from.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH,
                        "//div[@id='FlightSearchForm_ONE_WAY']/div/div/div/div[2]/div/div/div[2]/div/button").click()
    going_to = driver.find_element(By.XPATH, "//div[@id='destination_select-menu']/section/div/div/div/input")
    going_to.send_keys("Toronto")
    going_to.send_keys(Keys.ENTER)
    time.sleep(5)

    driver.find_element(By.ID, "search_button").click()
    time.sleep(10)
    success_search = driver.find_element(By.XPATH,
                                "//h5[normalize-space()='Recommended departing flights']").text
    assert "Please correct the error to continue" == success_search, "test failed"

def test_empty_departure_destination_one_way_flight_search():
    driver.get("https://www.expedia.ca/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[contains(.,'Flights')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@id='search_form_product_selector_flights']/div/div/div/ul/li[2]/a/span").click()
    time.sleep(3)

    driver.find_element(By.ID, "search_button").click()
    time.sleep(10)

    success_search = driver.find_element(By.XPATH,
                                "//h3[normalize-space()='Please correct the 2 errors to continue']").text
    assert "Please correct the 2 errors to continue" == success_search, "test failed"