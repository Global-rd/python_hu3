from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import page_elements as selec

class Scraper:
    def __init__(self):
        self.browser = None

    def start_browser(self):
        # Böngésző elindítása
        self.browser = webdriver.Chrome()

    def get_top_tags(self):
        # Megnyitjuk a főoldalt és kigyűjtjük a kategóriák linkjeit [cite: 5]
        self.browser.get(selec.BASE_URL)
        time.sleep(2)
        
        links = []
        for xpath in selec.TOP_TAG_XPATHS:
            element = self.browser.find_element(By.XPATH, xpath)
            url = element.get_attribute('href')
            links.append(url)
        return links

    def get_quotes_from_page(self, current_tag):
        # Egy adott oldalon lévő összes idézet összegyűjtése [cite: 6, 7]
        page_results = []
        containers = self.browser.find_elements(By.XPATH, selec.QUOTE_BOX)
        
        for item in containers:
            text = item.find_element(By.XPATH, selec.QUOTE_TEXT).text
            author = item.find_element(By.XPATH, selec.AUTHOR_NAME).text
            
            page_results.append({
                "tag": current_tag,
                "author": author,
                "quote": text
            })
        return page_results

    def scrape_all_from_tag(self, tag_url):
        # Végigmegy egy kategória összes oldalán (lapozás) [cite: 8, 9]
        tag_name = tag_url.split('/')[-2]
        all_data = []
        target_url = tag_url
        
        while True:
            self.browser.get(target_url)
            # Idézetek begyűjtése az aktuális oldalról
            current_quotes = self.get_quotes_from_page(tag_name)
            all_data.extend(current_quotes)

            try:
                # Megpróbálunk a következő oldalra lépni [cite: 10]
                next_btn = self.browser.find_element(By.XPATH, selec.NEXT_PAGE_BUTTON)
                next_btn.click()
                target_url = self.browser.current_url
                time.sleep(1)
            except NoSuchElementException:
                # Ha nincs több oldal, kilépünk a ciklusból
                break
                
        return all_data

    def save_to_csv(self, data_list, file_path):
        # Adatok mentése CSV fájlba pandas segítségével [cite: 12]
        df = pd.DataFrame(data_list)
        df.to_csv(file_path, index=False, encoding="utf-8-sig")