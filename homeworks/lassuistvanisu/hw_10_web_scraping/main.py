from qts_scraper import get_top_tags, get_driver, scrape_quotes_for_tag
import pandas as pd  

def main():
    driver = get_driver()
    all_rows = []

    try:
        top_tags = get_top_tags(driver)
        print("Top 10 tags:", top_tags)

        for tag in top_tags:
            print(f"Scraping tag: {tag}")
            tag_rows = scrape_quotes_for_tag(driver, tag)
            all_rows.extend(tag_rows)

    finally:
        driver.quit()

    # CSV creator
    df = pd.DataFrame(all_rows, columns=["tag", "author", "quote"])
    df.to_csv("homeworks\lassuistvanisu\hw_10_web_scraping\quotes_top10.csv", index=False, encoding="utf-8")

    print(f"CSV elkészült: quotes_top10.csv, sorok száma: {len(df)}")

if __name__ == "__main__":
    main()
