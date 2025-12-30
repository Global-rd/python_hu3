from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


BASE_URL = "https://quotes.toscrape.com"

#Chrome strat ini
def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

# TOP 10 scrape
def get_top_tags(driver):
    driver.get(BASE_URL)
    top_tags_block = driver.find_element(By.CSS_SELECTOR, ".col-md-4.tags-box")
    tag_elements = top_tags_block.find_elements(By.CSS_SELECTOR, "span.tag-item a")
    top_tags = [el.text.strip() for el in tag_elements]
    return top_tags

# Collection of quotes based on the top 10 tags
def scrape_quotes_for_tag(driver, tag):
    page = 1
    datas = []

    while True:
        url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        driver.get(url)

        #If there is no quote at this URL, we move on.
        if "No quotes found!" in driver.page_source:
            break

        quote_blocks = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        if not quote_blocks:
            break

        for qb in quote_blocks:
            text = qb.find_element(By.CSS_SELECTOR, "span.text").text.strip()
            author = qb.find_element(By.CSS_SELECTOR, "small.author").text.strip()
            datas.append({
                "tag": tag,          
                "author": author,
                "quote": text
            })

        # pagination management
        try:
            driver.find_element(By.CSS_SELECTOR, "li.next a")
            page += 1
        except NoSuchElementException:
            break

        time.sleep(0.3)

    return datas

