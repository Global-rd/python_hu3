from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
from dotenv import load_dotenv


load_dotenv()


def auto_login(driver, username, password):
    driver.get("https://quotes.toscrape.com/login")
    time.sleep(1)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(1)


USERNAME = os.getenv("QUOTES_USERNAME")
PASSWORD = os.getenv("QUOTES_PASSWORD")

if not USERNAME or not PASSWORD:
    raise RuntimeError(
        "Hiányzó környezeti változó: QUOTES_USERNAME vagy QUOTES_PASSWORD")

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--disable-usb-discovery")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

auto_login(driver, USERNAME, PASSWORD)

BASE_URL = "https://quotes.toscrape.com"
driver.get(BASE_URL)
time.sleep(1)

top_tags = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
top_10_tags = [tag.text for tag in top_tags]

print("Top 10 tag:", top_10_tags)

data = []

for tag in top_10_tags:
    driver.get(f"{BASE_URL}/tag/{tag}/")
    time.sleep(1)

    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for q in quotes:
            quote_text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text

            data.append({
                "tag": tag,
                "author": author,
                "quote": quote_text
            })

        try:
            driver.find_element(By.CSS_SELECTOR, "li.next a").click()
            time.sleep(1)
        except:
            break

df = pd.DataFrame(data)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUB_DIR = "top_10"

output_dir = os.path.join(BASE_DIR, SUB_DIR)
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "top_10_tags_quotes.csv")
df.to_csv(output_path, index=False, encoding="utf-8")

driver.quit()
print(f"Scraping kész! CSV fájl létrehozva: {output_path}")
