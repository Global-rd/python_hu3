from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import time


def get_top_10_tags(driver):
    driver.get("https://quotes.toscrape.com/")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tag-item"))
    )
    
    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tags-box .tag-item")
    top_10_tags = []
    
    for tag_elem in tag_elements[:10]:
        tag_link = tag_elem.find_element(By.CLASS_NAME, "tag")
        tag_name = tag_link.text.strip()
        top_10_tags.append(tag_name)
    
    print(f"Top 10 tag: {top_10_tags}")
    return top_10_tags


def scrape_tag_quotes(driver, tag_name):
    print(f"\n'{tag_name}' tag idézeteinek scrape-elése...")
    quotes_data = []
    page = 1
    
    while True:
        url = f"https://quotes.toscrape.com/tag/{tag_name}/page/{page}/"
        print(f"  Oldal {page} betöltése: {url}")
        driver.get(url)
        
        time.sleep(0.5)
        
        try:
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            
            if not quotes:
                print(f"  Nincs több idézet a(z) '{tag_name}' tag-nél.")
                break
            
            for quote in quotes:
                try:
                    text = quote.find_element(By.CLASS_NAME, "text").text.strip()
                    
                    author = quote.find_element(By.CLASS_NAME, "author").text.strip()
                    
                    
                    quotes_data.append({
                        'tag': tag_name,
                        'author': author,
                        'quote': text
                    })
                except NoSuchElementException:
                    
                    continue
            
            print(f"  {len(quotes)} idézet gyűjtve az {page}. oldalról")
            
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
                page += 1
            except NoSuchElementException:
                print(f"  Nincs több oldal a(z) '{tag_name}' tag-nél.")
                break
                
        except Exception as e:
            print(f"  Hiba történt: {e}")
            break
    
    print(f"Összesen {len(quotes_data)} idézet gyűjtve a(z) '{tag_name}' tag-hez")
    return quotes_data


def main():
    print("=" * 60)
    print("Quotes Scraper - Top 10 Tag-ek")
    print("=" * 60)
    print("\nSelenium driver indítása...")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        top_10_tags = get_top_10_tags(driver)
    
        all_quotes = []
        for i, tag in enumerate(top_10_tags, 1):
            print(f"\n[{i}/{len(top_10_tags)}] Feldolgozás...")
            tag_quotes = scrape_tag_quotes(driver, tag)
            all_quotes.extend(tag_quotes)
        
        output_file = 'quotes_top10_tags.csv'
        print("\n" + "=" * 60)
        print(f"CSV file létrehozása: {output_file}")
        print("=" * 60)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['tag', 'author', 'quote']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            writer.writerows(all_quotes)
        
        print(f"\nKész!")
        
    except Exception as e:
        print(f"\nHiba történt: {e}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
