import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd

df = pd.read_csv('your_path_to_csv_file')

URLS = df['links'].values

driver = webdriver.Safari()

try:
    for i in range(len(URLS)):
        url = URLS[i]
        print(f"Checking: {url}")
        try:
            driver.get(url)
            time.sleep(0.5)
            page_text = driver.page_source.lower()
        except WebDriverException as e:
            print("Browser error")
            continue

finally:
    driver.quit()
    print("Finished.")
