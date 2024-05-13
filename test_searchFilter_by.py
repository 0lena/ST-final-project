from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_filter_by_stops():
    driver.get(
        "https://www.expedia.ca/Flights-Search?flight-type=on&mode=search&trip=oneway&leg1=from%3AToronto%2C%20ON%2C%20Canada%20%28YYZ-Pearson%20Intl.%29%2Cto%3AMontreal%2C%20Canada%20%28YMQ-All%20Airports%29%2Cdeparture%3A27%2F05%2F2024TANYT%2CfromType%3AA%2CtoType%3AM&options=cabinclass%3Aeconomy&fromDate=27%2F05%2F2024&d1=2024-5-27&passengers=adults%3A1%2Cinfantinlap%3AN&pwaDialog=clientSideErrorDialog")
    driver.maximize_window()
    time.sleep(10)

    filter_by = driver.find_element(By.XPATH, "//input[@name='NUM_OF_STOPS']").click()
    driver.find_element(By.XPATH, "//*[@stid='FLIGHTS_DETAILS_AND_FARES-index-1-leg-0-fsr-FlightsActionButton']").click()
    time.sleep(5)

    success_nonstop = driver.find_element(By.XPATH,"//span[2]/h3").text
    assert "nonstop" in success_nonstop, "Test failed: 'nonstop' not found in the element text"

