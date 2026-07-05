# Web Scraping Portfolio

A collection of web scraping projects built with Python, Playwright, Stealth mode, and asynchronous API requests.

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

### 4. Quotes Scraper (Pagination)
- Scrapes all quotes from [quotes.toscrape.com](https://quotes.toscrape.com)
- Navigates through all pages using "Next" button
- Extracts: quote text and author
- Saves data to `quotes_all.json`
- Includes logging and error handling

### 5. API Parser: JSONPlaceholder Users
- Fetches user data from [JSONPlaceholder](https://jsonplaceholder.typicode.com) API
- Demonstrates asynchronous HTTP requests with `aiohttp`
- Extracts: name, email, city
- Saves data to `users.json`
- Uses `fake_useragent` for request masking

### 6. Wildberries Advanced Scraper
- Scrapes product data from [Wildberries.ru](https://www.wildberries.ru) (Calvin Klein)
- Extracts: product name, price, delivery date, link, article
- Uses Playwright Stealth and random delays
- Includes comprehensive logging and error handling
- Saves data to `config.json`

## 🛠️ Technologies Used

- Python 3.9+
- Playwright
- Playwright Stealth
- aiohttp (asynchronous HTTP requests)
- BeautifulSoup (optional)
- Pandas
- asyncio
- fake_useragent
- JSON

## 📦 Installation

```bash
pip install -r requirements.txt
playwright install
