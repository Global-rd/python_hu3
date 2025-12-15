from quotes_scraper import Scraper
import os
import time


def main():
    
    scraper = Scraper()
    
    BASE_URL = "https://quotes.toscrape.com/"
 
    URLS_FILE_PATH = "homeworks/fejeszsolt/hw_10_web_scraping/all_urls.txt"
    SCRAPED_DATA_PATH = "homeworks/fejeszsolt/hw_10_web_scraping/scraped_data.csv"

    data = []

    if os.path.exists(URLS_FILE_PATH):
        urls = scraper.read_urls_from_file(URLS_FILE_PATH)
    else:
        print("No URL list yet, reading from sitemap.")

        scraper.initialize_webdriver()

        urls = scraper.get_top_tag_urls(BASE_URL)

        scraper.write_urls_to_file(urls, URLS_FILE_PATH)

        scraper.driver.quit()

        print(f"Stored {len(urls)} in {URLS_FILE_PATH}")

    print(urls[:10])
    scraper.initialize_webdriver()


    for tag_url in urls:
        tag_name = tag_url.split('/')[-2]
        tag_quotes = scraper.scrape_tag_quotes(tag_url, tag_name)
        data.extend(tag_quotes)

    scraper.driver.quit()
    
    scraper.load_results_to_csv(data=data, filepath=SCRAPED_DATA_PATH)

if __name__ == "__main__":
    main()