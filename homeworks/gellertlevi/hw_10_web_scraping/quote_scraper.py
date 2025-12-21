import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://quotes.toscrape.com/"

def get_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_top_10_tags(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tags-box"))
    )
    tag_links = driver.find_elements(By.CSS_SELECTOR, "div.tags-box a.tag")
    top_tags = [link.text.strip() for link in tag_links[:10]]
    return top_tags

def scrape_quotes_for_tag(driver, tag):
    quotes_data = []
    page = 1
    while True:
        url = f"{BASE_URL}tag/{tag}/page/{page}/"
        driver.get(url)
        # Várunk, hogy vagy idézetek legyenek, vagy ne legyen találat
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.container"))
        )
        quote_cards = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        if not quote_cards:
            break
        for q in quote_cards:
            text_el = q.find_element(By.CSS_SELECTOR, "span.text")
            author_el = q.find_element(By.CSS_SELECTOR, "small.author")
            quotes_data.append({
                "tag": tag,
                "author": author_el.text.strip(),
                "quote": text_el.text.strip().strip("“”")
            })
        page += 1
        sleep(0.3)
    return quotes_data

def main(output_csv="quotes_top10_tags.csv"):
    driver = get_driver(headless=True)
    try:
        top_tags = get_top_10_tags(driver)
        all_rows = []
        for tag in top_tags:
            rows = scrape_quotes_for_tag(driver, tag)
            all_rows.extend(rows)
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"Sikeresen elkészült: {output_csv} (összes sor: {len(all_rows)})")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
