import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_CSV = "quotes.csv"

def scrape_quotes():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    
    quotes_data = []

    try:
        while True:
            # Wait until quotes are loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
            )
            
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            for quote in quotes:
                text = quote.find_element(By.CLASS_NAME, "text").text
                author = quote.find_element(By.CLASS_NAME, "author").text
                tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
                quotes_data.append({
                    "text": text,
                    "author": author,
                    "tags": ", ".join(tags)
                })
            # Check for the next page
            try:
                next_button = driver.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME, "a")
                next_button.click()
                time.sleep(2)  # Wait for the next page to load
            except NoSuchElementException:
                break  # No more pages, exit the loop
    except TimeoutException:
        print("Loading took too much time!")
    finally:
        driver.quit()

    # Save the data to a CSV file
    df = pd.DataFrame(quotes_data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Scraped {len(quotes_data)} quotes and saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    scrape_quotes()