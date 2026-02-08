# main.py

from quotes_scraper import QuotesScraper
import os

def main():
    
    scraper = QuotesScraper()
    
    OUTPUT_FILE = "quotes_results.csv"

    scraper.initialize_webdriver()
    
    all_scraped_data = []
    
    try:
        
        top_tags = scraper.get_top_10_tags()
        print(f"Megtalált tagek a feldolgozáshoz: {top_tags}")
        
        
        for tag in top_tags:
            tag_data = scraper.scrape_quotes_for_tag(tag)
            all_scraped_data.extend(tag_data)
            
        
        scraper.save_to_csv(all_scraped_data, OUTPUT_FILE)
        
    finally:
        scraper.close()

if __name__ == "__main__":
    main()