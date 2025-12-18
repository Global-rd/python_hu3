# https://quotes.toscrape.com/tag/inspirational/page/1/
# 
# <li class="next">
#      <a href="/tag/love/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
# </li>
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options   
from selenium.webdriver.common.by import By
import pandas as pd
import time

def main():

    URL = "https://quotes.toscrape.com/"

    # A Selenium automatikusan letölti a megfelelő drivert
    driver = webdriver.Chrome()

    driver.get(URL)
    time.sleep(10)

    # col-md-4 tags-box: "Top Ten tags"
    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
    tags = [tag.text for tag in tag_elements]
    print("Top Ten tags:", tags)
    
    data = []

    # összes tag összes oldalán végigmegyek
    print("Starting scraping quotes...")

    for tag in tags:
        
        page = 1
        
        while True:
    
            url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
            driver.get(url)
            time.sleep(2)

            quotes = driver.find_elements(By.CLASS_NAME, "quote")

            for quote in quotes:
                text = quote.find_element(By.CLASS_NAME, "text").text
                author = quote.find_element(By.CLASS_NAME, "author").text
                data.append({"tag": tag, "author": author, "quote": text})

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, ".next a")
                page += 1 
            except:
                print(f"No more pages for this tag: {tag}/{page}")
                break   
               
    # adatok mentése CSV fájlba
    df = pd.DataFrame(data)
    print(f"Total quotes scraped: {len(df)}")

    df.to_csv("quotes.csv", index=False, encoding="utf-8")
    print("End of scraping. Data saved to quotes.csv")

    sleep_time = 10
    print(f"Waiting {sleep_time} seconds before closing the driver...")
    time.sleep(sleep_time)

    driver.quit()
    

if __name__ == "__main__":
    main()