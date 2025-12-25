import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from datetime import datetime as dt
import pandas as pd

import toscrape_selectors as toscrape


class ToScrapeScraper:

    def scrape_top10_tags(self, url):

        #print(f"Scraping Top 10 tags from {url}")

        self.driver.get(url)
        tags = self.driver.find_elements(by=By.XPATH, value=toscrape.TOP10_TAGS_XPATH)  
        tags_texts = [element.text for element in tags]
        #print(tags_texts)

        return tags


    def scrape_quote(self, quote_xpath):   
     
        quote = self.driver.find_element(by=By.XPATH, value=quote_xpath + "/span[1]") 

        return quote.text
    

    def scrape_author(self, quote_xpath):
        
        author = self.driver.find_element(by=By.XPATH, value=quote_xpath + "/span[2]/small") 

        return author.text


    def scrape_quotes(self, url, tag):

        self.driver.get(url)

        quote_elements = self.driver.find_elements(by=By.XPATH, value=toscrape.QUOTE_XPATH)  
        quote_counrt = quote_elements.__len__()
        print(f'Total quotes found: {quote_counrt}')    
                
        quotes =[]
        for counter in range(1,quote_counrt+1):

            quote_xpath = toscrape.QUOTE_XPATH + f'[{counter}]'

            quote_text = self.scrape_quote(quote_xpath)
            author_text = self.scrape_author(quote_xpath)

            quote = {
                "tag": tag,     
                "quote": quote_text,
                "author": author_text
            }
            quotes.append(quote)    
            #print(f'{tag} - "{quote_text}" - {author_text}')
        
        return quotes

    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
    
    @staticmethod
    def load_results_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)