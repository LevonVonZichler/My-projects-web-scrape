# Web Scraping Portfolio

A collection of web scraping projects built with Python, Playwright, and Stealth mode.

## 🚀 Projects

### 1. Quotes Scraper (Infinite Scroll)
- Scrapes quotes from [quotes.toscrape.com/scroll](http://quotes.toscrape.com/scroll)
- Uses infinite scroll to load all quotes
- Extracts: text, author, tags
- Saves data to `books.json`

### 2. Wildberries Parser
- Scrapes product data from [Wildberries.ru](https://www.wildberries.ru)
- Extracts: product name, price, delivery date
- Uses Playwright Stealth to avoid detection
- Exports data to `wb_products.json`
- Includes logging and error handling

### 3. Books to Scrape
- Scrapes book data from [books.toscrape.com](https://books.toscrape.com)
- Navigates through pagination (1000+ books)
- Extracts: title, price, stock, description
- Saves data to `books.csv`

## 🛠️ Technologies Used

- Python 3.9+
- Playwright
- Playwright Stealth
- BeautifulSoup (optional)
- Pandas
- asyncio

## 📦 Installation

```bash
pip install -r requirements.txt
playwright install
