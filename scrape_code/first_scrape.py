from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def get_driver():
    options=webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")

    driver =webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver =get_driver()
    time.sleep(2)
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

def clean_text(text):
    """Extract only the temperature from text"""
    output =text.split(": ")
    print(output)
    return float(output[1])
    

print(main())

