
from pathlib import Path
from quotes_scraper import QuotesScraper as QS
import pandas as pd


def main():
    #print("START main()")
    #print("Working dir:", Path.cwd())

    scraper = None  # VS Code / Pylance miatt szükséges

    try:
        scraper = QS()
        print("WebDriver started")

        top_tags = scraper.get_top_10_tags()
        print("Top tags:", top_tags)
        print("Top tags count:", len(top_tags))

        all_data = []

        for tag in top_tags:
            tag_data = scraper.scrape_quotes_by_tag(tag)
            print(f"Tag '{tag}' -> {len(tag_data)} quotes")
            all_data.extend(tag_data)

        print("Total rows:", len(all_data))

        df = pd.DataFrame(all_data)
        out_path = Path(__file__).resolve().parent / "quotes.csv"
        df.to_csv(out_path, index=False, encoding="utf-8-sig")
        #print("CSV saved to:", out_path)

    finally:
        if scraper is not None:
            scraper.driver.quit()
            print("WebDriver closed")

    print("END main()")


if __name__ == "__main__":
    main()
