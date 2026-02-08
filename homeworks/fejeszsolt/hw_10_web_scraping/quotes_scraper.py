import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime as dt
import pandas as pd
import time

import quotes_selectors as selec


class Scraper:
      def __init__(self):
        self.driver = None
      def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

      def get_top_tag_urls(self, initial_url):
        self.driver.get(initial_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selec.TOP_1)))
        top_tag_urls = []
        for xpath in selec.TOP_TAGS_LIST: 
            tag_element = self.driver.find_element(By.XPATH, xpath)
            tag_link = tag_element.get_attribute('href')
            top_tag_urls.append(tag_link)
        return top_tag_urls



      def get_quote_text(self, container):
        quote_element = container.find_element(By.XPATH, selec.QUOTE_TEXT_XPATH)
        return quote_element.text


      def get_author_name(self, container):
        author_element = container.find_element(By.XPATH, selec.AUTHOR_PATH_XPATH)
        return author_element.text

      def scrape_page(self, tag_name):
        page_data = [] 
        quote_containers = self.driver.find_elements(By.XPATH, selec.QUOTE_CONTAINER_XPATH)
        for container in quote_containers:
            quote_text = self.get_quote_text(container)
            author_name = self.get_author_name(container)
            page_data.append({
                "quote": quote_text,
                "author": author_name,
                "tag": tag_name
                })               
        return page_data

      def scrape_tag_quotes(self, tag_url, tag_name):
        all_tag_quotes = []
        current_url = tag_url 
        
        while True:
            self.driver.get(current_url)
            current_page_data = self.scrape_page(tag_name)
            all_tag_quotes.extend(current_page_data)


            try:
                next_button = self.driver.find_element(By.XPATH, selec.NEXT_BUTTON_PATH)
                next_button.click() 
                current_url = self.driver.current_url               
                time.sleep(1.5)
                
            except NoSuchElementException:
                break
                
        return all_tag_quotes

      @staticmethod
      def write_urls_to_file(urls, file_name):
        with open(file_name, "w") as file:
            for url in urls:
                file.write(url + "\n")
        print(f"URLs has been written to {file_name}")

      @staticmethod
      def read_urls_from_file(file_name):
        urls = []
        with open(file_name, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls
    
      @staticmethod
      def load_results_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)