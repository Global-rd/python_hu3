from scraper_logic import Scraper
import os

def main():
    scraper = Scraper()
    
    # Mappa
    folder_name = "homeworks/olahsandor/hw_10_web_scraping"
          
    csv_output = f"{folder_name}/scraped_data.csv"

    print("Program starting...")
    scraper.start_browser()

    # 1. Top 10 kategória linkjeinek megszerzése
    tag_links = scraper.get_top_tags()

    final_results = []

    # 2. Idézetek gyűjtése minden kategóriához [cite: 3]
    for link in tag_links:
        print(f"Data collecting: {link}")
        tag_data = scraper.scrape_all_from_tag(link)
        final_results.extend(tag_data)

    # 3. Mentés és lezárás
    scraper.save_to_csv(final_results, csv_output)
    
    print(f"Saved: {len(final_results)} quotes.")
    scraper.browser.quit()

if __name__ == "__main__":
    main()