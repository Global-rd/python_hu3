import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://quotes.toscrape.com/tag/{tag}/page/{page}/"


def get_top_tags(driver):
    driver.get("https://quotes.toscrape.com/")
    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a.tag")
    top_10 = [t.text.strip() for t in tag_elements[:10]]
    return top_10


def scrape_quotes_of_tag(driver, tag):
    quotes_for_tag = []
    page = 1

    while True:
        url = BASE_URL.format(tag=tag, page=page)
        driver.get(url)

        # VÁRUNK, hogy a .quote elemek biztosan megjelenjenek
        try:
            quote_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote"))
            )
        except:
            break  # ha nincs több quote elem → vége

        for quote in quote_elements:
            text = quote.find_element(By.CLASS_NAME, "text").text.strip()
            author = quote.find_element(By.CLASS_NAME, "author").text.strip()

            quotes_for_tag.append({
                "tag": tag,
                "author": author,
                "quote": text
            })

        page += 1

    return quotes_for_tag


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    top_tags = get_top_tags(driver)

    all_quotes = []
    for tag in top_tags:
        tag_quotes = scrape_quotes_of_tag(driver, tag)
        all_quotes.extend(tag_quotes)

    driver.quit()

    with open("quotes_scraped.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(all_quotes)


if __name__ == "__main__":
    main()





