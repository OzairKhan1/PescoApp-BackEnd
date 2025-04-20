# backend/selenium_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_customer_id(account_number):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bill.pitc.com.pk/pescobill")
        time.sleep(2)

        acc_str = str(account_number).zfill(14)
        input_box = wait.until(EC.presence_of_element_located((By.ID, "searchTextBox")))
        input_box.clear()
        input_box.send_keys(acc_str)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        consumer_id_td = driver.find_element(
            By.XPATH,
            "//tr[contains(@class,'fontsize') and contains(@class,'content')]/td[1]"
        )
        consumer_id = consumer_id_td.text.strip()

    except Exception as e:
        consumer_id = ""
        print(f"Error: {e}")
    finally:
        driver.quit()

    return consumer_id
