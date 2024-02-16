from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

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

def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        time.sleep(3)

scroll_down(driver)

links = []

for i in range(132):
    tile = driver.find_elements(By.CSS_SELECTOR, "a.link")[i+3]  
    tile.click()
    time.sleep(40)  # Adjust this wait time as needed
    links.append(driver.current_url)
    driver.back()  # Go back to the main page
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.link")))  # Wait for the tiles to reload
    scroll_down(driver)



# Save links in a csv file
with open('links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in links:
        writer.writerow([link])

print(links)

driver.quit()  # Don't forget to quit the driver at the end
