from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json

url = "https://tulser.askme.nl/app3/#/home"
user_name = "r.kouwenberg@tulser.com"
password = "Learnlinq9!"

option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=option)

driver.get(url)

wait = WebDriverWait(driver, 60)

# Wait for the login form elements to be present
username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#username")))
password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#password")))
submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

# Fill in login form and submit
username_input.send_keys(user_name)
password_input.send_keys(password)
submit_button.click()

# Wait for the page to fully load after login
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.link")))

link = "https://tulser.askme.nl/app3/#/askme/aba5ba80-77e3-4b11-a3e4-8cfc31bd1405?title=Begeleiden-bij-zelfstandig-in-en-uit-bed-komen-(AZB)"

link2 = "https://tulser.askme.nl/app3/#/askme/c704f8b0-57b3-480b-8656-2a0532c9e728?title=Steunkousen"

link3 = "https://tulser.askme.nl/app3/#/askme/24aae625-0636-45cc-894b-282ff11512ba?title=Katheterzorg"


driver.get(link2)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item__text-wrap")))

title = driver.find_element(By.TAG_NAME, "h1").text

data = {
    title : {}
}

level1_elements = driver.find_elements(By.CSS_SELECTOR, ".item__text-wrap")

for level1 in level1_elements:
    data[title][level1.text] = {
        
    }

    level1.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.level2")))
    level2_elements = driver.find_elements(By.CSS_SELECTOR, "li.level2")

    if len(level2_elements) == 1:
        data[title][level1.text][level2_elements[0].text] = {}
        
        pgrid_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pgrid-content__content-center")))
        level3_elements = pgrid_content.find_elements(By.TAG_NAME, "li")

        if len(level3_elements) == 1:
            data[title][level1.text][level2_elements[0].text][level3_elements[0].text] = {}
        elif len(level3_elements) > 1:
            for level3 in level3_elements:
                data[title][level1.text][level2_elements[0].text][level3.text] = {}
    
    elif len(level2_elements) > 1:
        for level2 in level2_elements:
            data[title][level1.text][level2.text] = {}

            level2.click()

            pgrid_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pgrid-content__content-center")))
            level3_elements = pgrid_content.find_elements(By.TAG_NAME, "li")

            if len(level3_elements) == 1:
                data[title][level1.text][level2.text][level3_elements[0].text] = {}
            elif len(level3_elements) > 1:
                for level3 in level3_elements:
                    data[title][level1.text][level2.text][level3.text] = {}
            
            level2.click()


    
    level1.click()
    time.sleep(3)













with open('data2.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file,ensure_ascii=False, indent=4)

print(data)

