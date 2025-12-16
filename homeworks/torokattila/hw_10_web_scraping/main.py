from quotes_scraper import QuotesScraper

SCRAPED_DATA_PATH = "homeworks/torokattila/hw_10_web_scraping/quotes.csv"

scraper = QuotesScraper()

urls = scraper.get_top10_tag_url()
data = scraper.scrape_urls(urls)

for row in data:
    print(row)

print("Összes találat:", len(data))

scraper.save_to_csv(data, SCRAPED_DATA_PATH)

print("Kész:", len(data), "CSV-be mentve")
