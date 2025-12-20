from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import quotes_selectors as qs


class QuotesScraper:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def get_top_10_tags(self):
        self.driver.get("https://quotes.toscrape.com/")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, qs.TOP_TAGS_XPATH))
        )

        tags = self.driver.find_elements(By.XPATH, qs.TOP_TAGS_XPATH)
        return [t.text.strip() for t in tags if t.text.strip()]

    def scrape_quotes_by_tag(self, tag):
        data = []
        url = f"https://quotes.toscrape.com/tag/{tag}/"

        while True:
            self.driver.get(url)

            quotes = self.driver.find_elements(By.XPATH, qs.QUOTE_BLOCK_XPATH)
            for q in quotes:
                text = q.find_element(By.XPATH, qs.QUOTE_TEXT_XPATH).text
                author = q.find_element(By.XPATH, qs.AUTHOR_XPATH).text

                data.append({
                    "tag": tag,
                    "author": author,
                    "quote": text
                })

            try:
                next_btn = self.driver.find_element(By.XPATH, qs.NEXT_BUTTON_XPATH)
                url = next_btn.get_attribute("href")
            except:
                break
            

        return data
