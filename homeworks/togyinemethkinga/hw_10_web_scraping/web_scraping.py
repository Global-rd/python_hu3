from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pathlib import Path

url = "https://quotes.toscrape.com/"
output_file = Path("homeworks") / "togyinemethkinga" / "hw_10_web_scraping" / "top_10_quotes.csv"

driver = webdriver.Chrome()
all_quotes = []
    
try:
    # weblap megnyitása:
    driver.get(url)
    wait = WebDriverWait(driver, 10)
        
    # Top 10 tag listába gyűjtése:
    top_tags = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tags-box")))
    tags = [tag.text for tag in top_tags.find_elements(By.TAG_NAME, "a")[:10]]
        
    # A tag-ekhez tartozó idézetek kigyűjtése
    for tag in tags:
        tag_url = f"{url}tag/{tag}/"
            
        while True:
            driver.get(tag_url)
            # Idézetek betöltésének megvárása
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
            # Idézetek kinyerése az aktuális oldalról
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            for quote in quotes:
                quote_text = quote.find_element(By.CLASS_NAME, "text").text
                author = quote.find_element(By.CLASS_NAME, "author").text
                all_quotes.append({
                    "tag": tag,
                    "author": author,
                    "quote": quote_text
                    })
            # Következő oldal:
            try:
                next_button = driver.find_element(By.CLASS_NAME, "next")
                next_page = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
                tag_url = next_page
            except:
                break
        
    # Adatok mentése csv fájlba
    df = pd.DataFrame(all_quotes)
    df.to_csv(output_file, index=False)

    print(f"Adatok sikeresen kimentve: {output_file}")

except Exception as e:
    print(f"Hiba a scraping közben: {e}")
    
finally:
    driver.quit()