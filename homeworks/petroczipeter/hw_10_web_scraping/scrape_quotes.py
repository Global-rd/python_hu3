from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

BASE_URL = "https://quotes.toscrape.com"
RESULTS = []

driver = webdriver.Chrome()
driver.get(BASE_URL)
time.sleep(1)

# 1️ Top 10 tag összegyűjtése
top_tags = driver.find_elements(By.CSS_SELECTOR, ".tags-box a.tag")
top_tags = [tag.text for tag in top_tags[:10]]

print("Top 10 tag:", top_tags)

# 2️ Tag-enként scrape
for tag in top_tags:
    tag_url = f"{BASE_URL}/tag/{tag}/"
    driver.get(tag_url)
    time.sleep(1)

    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text

            RESULTS.append({
                "tag": tag,
                "author": author,
                "quote": text
            })

        # pagination
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_button.click()
            time.sleep(1)
        except:
            break

driver.quit()

# 3️ CSV mentés
df = pd.DataFrame(RESULTS)
df.to_csv("quotes.csv", index=False, encoding="utf-8")

print("Kész! quotes.csv létrehozva.")