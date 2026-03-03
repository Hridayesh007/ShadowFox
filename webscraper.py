import scrapy
from scrapy.crawler import CrawlerProcess
import logging

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]
    
    # 1. Store data in CSV automatically using Scrapy's built-in Feed Exports
    custom_settings = {
        'FEEDS': {
            'scraped_quotes.csv': {
                'format': 'csv',
                'overwrite': True, # Overwrites the file each time you run the script
            }
        },
        # Suppress overly verbose Scrapy logs for a cleaner terminal output
        'LOG_LEVEL': 'INFO' 
    }

    def parse(self, response):
        self.logger.info(f"Successfully connected to {response.url}")
        
        quotes = response.css('div.quote')
        
        # Loop through each quote on the page
        for quote in quotes:
            # 2. Add Error Handling
            try:
                text = quote.css('span.text::text').get()
                author = quote.css('small.author::text').get()
                tags = quote.css('a.tag::text').getall()
                
                # Yielding a dictionary automatically passes the data to the CSV
                yield {
                    'Quote': text,
                    'Author': author,
                    'Tags': ", ".join(tags)
                }
            except Exception as e:
                # If a specific quote has broken HTML, log the error and continue
                self.logger.error(f"Failed to parse a quote due to: {e}")

        # 3. Scrape Multiple Pages (Pagination)
        # Look for the 'Next' button at the bottom of the page
        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            self.logger.info(f"Found next page: {next_page}. Following link...")
            # Automatically follow the link and pass it back to this same parse method
            yield response.follow(next_page, callback=self.parse)
        else:
            self.logger.info("No more pages found. Scraping complete!")

# --- Main Execution ---
if __name__ == "__main__":
    print("Starting Advanced Scrapy Spider...")
    
    # Initialize and start the Scrapy crawler inside this script
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start() 
    
    print("Check 'scraped_quotes.csv' for your data!")