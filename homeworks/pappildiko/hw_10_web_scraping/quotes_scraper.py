from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
import quotes_selectors as sel


class QuotesScraper:
    def __init__(self):
        self.driver = None

    def initialize_webdriver(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def get_top_tags(self, url, top_n=10):
        self.driver.get(url)
        time.sleep(1)
        tags_elements = self.driver.find_elements(By.CSS_SELECTOR, sel.TOP_TAGS_CSS)
        top_tags = [t.text for t in tags_elements][:top_n]
        return top_tags

    def scrape_quotes_for_tag(self, tag, base_url="https://quotes.toscrape.com/tag/"):
        tag_url = f"{base_url}{tag}/"
        self.driver.get(tag_url)
        time.sleep(1)

        all_quotes = []
        page_num = 1

        while True:
            quotes_elements = self.driver.find_elements(By.CSS_SELECTOR, sel.QUOTE_ITEM_CSS)

            for q in quotes_elements:
                text = q.find_element(By.CSS_SELECTOR, sel.QUOTE_TEXT_CSS).text
                author = q.find_element(By.CSS_SELECTOR, sel.QUOTE_AUTHOR_CSS).text

                all_quotes.append({
                    "tag": tag,
                    "author": author,
                    "quote": text
                })

            
            print(f"[Tag: {tag}] Page {page_num} scraped, total quotes so far: {len(all_quotes)}")

            
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, sel.NEXT_BUTTON_CSS)
                next_button.click()
                page_num += 1
                time.sleep(1)
            except:
                print(f"[Tag: {tag}] Finished scraping, total quotes: {len(all_quotes)}\n")
                break

        return all_quotes

    @staticmethod
    def load_results_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding="utf-8")
