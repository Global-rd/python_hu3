from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import quotes_selector as QS
import csv


class QuotesScraper:

    def get_top10_tag_url(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(QS.URL)

        wait = WebDriverWait(driver, QS.TIMEOUT)
        wait.until(EC.presence_of_element_located((By.XPATH, QS.TOP_TAGS_XPATH)))

        tag_links = driver.find_elements(By.XPATH, QS.TOP_TAGS_XPATH)
        urls = [e.get_attribute("href") for e in tag_links]  # 10 db
        driver.quit()
        return urls

    def scrape_urls(self, urls):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, QS.TIMEOUT)

        results = []
        try:
            for start_url in urls:
                driver.get(start_url)

                # tag név a tag URL-ből
                # pl: https://quotes.toscrape.com/tag/love/ -> love
                tag_name = start_url.split("/tag/")[1].split("/")[0]

                while True:
                    wait.until(
                        EC.presence_of_all_elements_located((By.XPATH, QS.QUOTE_BLOCKS))
                    )
                    blocks = driver.find_elements(By.XPATH, QS.QUOTE_BLOCKS)

                    for b in blocks:
                        text = b.find_element(By.XPATH, QS.QUOTE_TEXT).text
                        author = b.find_element(By.XPATH, QS.QUOTE_AUTHOR).text
                        results.append(
                            {"tag": tag_name, "author": author, "quote": text}
                        )

                    next_btn = driver.find_elements(By.XPATH, QS.NEXT_BUTTON)
                    if next_btn:
                        next_url = next_btn[0].get_attribute("href")
                        driver.get(next_url)
                    else:
                        break

        finally:
            driver.quit()

        return results

    def save_to_csv(self, data, filename="quotes.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
            writer.writeheader()
            writer.writerows(data)
