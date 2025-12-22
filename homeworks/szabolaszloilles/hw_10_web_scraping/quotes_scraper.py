# quotes_scraper.py

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


import quotes_selectors as qs

class QuotesScraper:
    
    def __init__(self):
        self.base_url = "https://quotes.toscrape.com"
        self.driver = None

    def initialize_webdriver(self):
        """Elindítja a Chrome böngészőt."""
        options = Options()
        
        self.driver = webdriver.Chrome(options=options)

    def get_top_10_tags(self):
        """Lescrape-eli a top 10 tag nevét a főoldalról."""
        print("Top 10 tag gyűjtése...")
        self.driver.get(self.base_url)
        
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, qs.TOP_TAGS_XPATH))
        )
        
        tag_elements = self.driver.find_elements(By.XPATH, qs.TOP_TAGS_XPATH)
        tags = [tag.text for tag in tag_elements]
        
       
        return tags[:10]

    def scrape_quotes_for_tag(self, tag):
        """
        Végigmegy egy adott tag összes oldalán (pagination) 
        és kigyűjti az idézeteket.
        """
        print(f"--- '{tag}' tag feldolgozása ---")
        
        current_url = f"{self.base_url}/tag/{tag}"
        self.driver.get(current_url)
        
        quotes_data = []
        
        while True:
           
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, qs.QUOTE_BLOCK_XPATH))
                )
                
                quote_blocks = self.driver.find_elements(By.XPATH, qs.QUOTE_BLOCK_XPATH)
                
                for block in quote_blocks:
                    text = block.find_element(By.XPATH, qs.QUOTE_TEXT_XPATH).text
                    author = block.find_element(By.XPATH, qs.AUTHOR_XPATH).text
                    
                    
                    quotes_data.append({
                        "tag": tag,
                        "author": author,
                        "quote": text
                    })
            except Exception as e:
                print(f"Hiba az adatok olvasásakor: {e}")

            
            try:
                next_button = self.driver.find_element(By.XPATH, qs.NEXT_PAGE_XPATH)
                next_button.click()
                time.sleep(1) 
            except NoSuchElementException:
                print(f"Nincs több oldal a '{tag}' címkéhez.")
                break
                
        return quotes_data

    def save_to_csv(self, data, filename):
        """Mentés CSV-be pandas segítségével."""
        df = pd.DataFrame(data)
        
        if not data:
            print("Nincs menthető adat.")
            return

        df = df[['tag', 'author', 'quote']]
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Sikeres mentés: {filename}")

    def close(self):
        if self.driver:
            self.driver.quit()