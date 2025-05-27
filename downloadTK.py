import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd

df = pd.read_csv('/Applications/PLIKI/MN24/DMWS/law_nlp/dane_TK_04-09.csv')

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
