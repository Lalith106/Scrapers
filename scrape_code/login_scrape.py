from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from datetime import datetime as dt
from selenium.webdriver.common.keys import Keys

def get_driver():
    options=webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")

    driver =webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver =get_driver()
    driver.find_element(By.ID,"id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID,"id_password").send_keys('automatedautomated'+Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)
    driver.find_element(By.XPATH,"/html/body/nav/div/a").click()
    for _ in range(10):
        time.sleep(2)
        element = driver.find_element(By.XPATH,"/html/body/div[1]/h1[2]")
        create_file(parse_text(element))

def parse_text(element):
    text=element.text.split(":")
    print(float(text[1]))
    return float(text[1])

def create_file(value):
    timestamp =dt.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename= f'data_{timestamp}.txt'
    with open(filename,'w') as f:
        f.write(str(value))
    print(f"[+] saved: {filename}")

main()

