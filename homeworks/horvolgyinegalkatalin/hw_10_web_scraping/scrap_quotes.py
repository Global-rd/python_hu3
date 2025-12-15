from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_quotes():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    print("türelem, dolgozom!")

    driver.get("https://quotes.toscrape.com/")
    time.sleep(1)
    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
    top_10_tags = [tag.text for tag in tag_elements[:10]]
    print("első 10 tag", top_10_tags)
    data = []

    # összes tag összes oldalán végigmegyek
    print("türelem, dolgozom!")

    for tag in top_10_tags:
        page = 1
        while True:
            url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
            driver.get(url)
            time.sleep(1)
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            if not quotes:
                break  # nincs több oldal
            for q in quotes:
                text = q.find_element(By.CLASS_NAME, "text").text
                author = q.find_element(By.CLASS_NAME, "author").text
                data.append({"tag": tag, "author": author, "quote": text})
            page += 1
    # végeredmény kiírása
    df = pd.DataFrame(data)
    df.to_csv("idézetek.csv", index=False, encoding="utf-8")
    driver.quit()
    print("kész a fájl")


if __name__ == "__main__":
    scrape_quotes()
