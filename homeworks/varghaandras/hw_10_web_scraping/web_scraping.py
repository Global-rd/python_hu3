import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_CSV = "quotes_top10_tags.csv"


def setup_driver(headless: bool = True):
    opts = webdriver.ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1280,1024")
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(30)
    return driver


def get_top10_tags(driver, wait):
    driver.get(BASE_URL)
    # Wait for the "Top Ten tags"
    tags_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[h2[contains(., 'Top Ten tags')]]")
        )
    )
    tag_links = tags_box.find_elements(By.CSS_SELECTOR, "a.tag")
    top_tags = []
    for a in tag_links:
        name = a.text.strip()
        href = a.get_attribute("href")
        if name and href:
            top_tags.append((name, href))
    return top_tags  # list: [(tag_name, absolute_url), ...]


def scrape_quotes_for_tag(driver, wait, tag_name, tag_url, seen):
    """
    Returns: list[dict(tag, author, quote)]
    'seen' is a set to avoid duplicates (key: (tag_name, quote_text))
    """
    rows = []
    next_url = tag_url

    while True:
        driver.get(next_url)
        # Wait until quotes are present on the page
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.quote")))
        quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")

        for q in quotes:
            # Quote text
            quote_text = q.find_element(By.CSS_SELECTOR, "span.text").text.strip()
            # Author name
            author = q.find_element(By.CSS_SELECTOR, "small.author").text.strip()

            key = (tag_name, quote_text)
            if key not in seen:
                seen.add(key)
                rows.append({"tag": tag_name, "author": author, "quote": quote_text})

        # Pagination: follow the "Next" link
        try:
            next_link = driver.find_element(By.CSS_SELECTOR, "li.next > a")
            next_url = next_link.get_attribute("href")
            # Small delay
            time.sleep(0.5)
        except NoSuchElementException:
            break

    return rows


def main():
    driver = setup_driver(headless=True)
    wait = WebDriverWait(driver, 15)
    all_rows = []
    seen = set()

    try:
        # 1) Collect Top Ten tag names and their URLs
        top_tags = get_top10_tags(driver, wait)
        print(f"Top 10 tags: {[t[0] for t in top_tags]}")

        # 2) Traverse each tag page and handle pagination
        for tag_name, tag_url in top_tags:
            print(f"Scraping: {tag_name} -> {tag_url}")
            rows = scrape_quotes_for_tag(driver, wait, tag_name, tag_url, seen)
            all_rows.extend(rows)
            print(f"  Collected quotes: {len(rows)}")

        # 3) Write results into CSV with pandas
        df = pd.DataFrame(all_rows, columns=["tag", "author", "quote"])
        # Use utf-8-sig for Excel compatibility
        df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

        print(f"Done! File: {OUTPUT_CSV}, total rows: {len(df)}")

    except TimeoutException as e:
        print("Timeout occurred:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
