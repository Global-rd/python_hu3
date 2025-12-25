from toscrape_scraper import ToScrapeScraper
import os
import time

def main():    
    scraper = ToScrapeScraper()    
    SCRAPED_DATA_PATH = "homeworks/kismoditamas/hw_10_web_scraping/scraped_toscrape_data.csv"


    scraper.initialize_webdriver()
    
    tags=[]
    tags = [tag.text for tag in scraper.scrape_top10_tags("https://quotes.toscrape.com")]
    
    data = []
    for tag in tags:
        print(f"Scraping quotes from '{tag}' page.")
        tagurl = f"https://quotes.toscrape.com/tag/{tag}/"
        
        quotes = scraper.scrape_quotes(tagurl, tag)
        data.extend(quotes)        
    
    scraper.load_results_to_csv(data=data, filepath=SCRAPED_DATA_PATH)
    scraper.driver.quit()

if __name__ == "__main__":
    main()