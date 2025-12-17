from quotes_scraper import QuotesScraper
import os

def main():
    scraper = QuotesScraper()
    OUTPUT_CSV = "top10_tags_quotes.csv"

    print("Initializing webdriver...")
    scraper.initialize_webdriver()

    print("Getting top 10 tags...")
    top_tags = scraper.get_top_tags("https://quotes.toscrape.com/")
    print("Top tags:", top_tags)

    all_data = []

    for tag in top_tags:
        print(f"Scraping quotes for tag: {tag}")
        tag_quotes = scraper.scrape_quotes_for_tag(tag)
        print(f"Found {len(tag_quotes)} quotes for tag {tag}")
        all_data.extend(tag_quotes)

    print(f"Saving {len(all_data)} quotes to CSV...")
    scraper.load_results_to_csv(all_data, OUTPUT_CSV)
    print(f"Done! CSV saved as {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
