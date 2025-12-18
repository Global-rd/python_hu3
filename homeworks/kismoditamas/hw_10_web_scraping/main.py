from toscrape_scraper import ToScrapeScraper
import os
import time


def main():
    
    scraper = ToScrapeScraper()
    #URLS_FILE_PATH = "homeworks/kismoditamas/hw_10_web_scraping/top10_urls.txt"
    SCRAPED_DATA_PATH = "homeworks/kismoditamas/hw_10_web_scraping/scraped_toscrape_data.csv"


    scraper.initialize_webdriver()
    urls = scraper.scrape_top10_tagurl("https://quotes.toscrape.com")


    print(urls[:10])
    
'''
    data = []
    for url in urls[:5]:
        product_data = scraper.scrape_product_data(url)
        print(product_data)
        data.append(product_data)
    
    scraper.load_results_to_csv(data=data, filepath=SCRAPED_DATA_PATH)
'''
if __name__ == "__main__":
    main()