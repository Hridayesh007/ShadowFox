import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://quotes.toscrape.com/page/{}/"


def scrape_quotes():
    page = 1
    all_quotes = []

    while True:
        url = BASE_URL.format(page)
        print(f"Scraping Page {page}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Error fetching page:", e)
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

            all_quotes.append({
                "text": text,
                "author": author,
                "tags": ", ".join(tags)
            })

        page += 1

    return all_quotes


def save_to_csv(data, filename="output.csv"):
    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"\nData saved to {filename}")


if __name__ == "__main__":
    quotes_data = scrape_quotes()

    if quotes_data:
        save_to_csv(quotes_data)
    else:
        print("No data scraped.")