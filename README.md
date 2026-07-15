# Web Scraping Portfolio

A collection of web scraping projects built with Python, Playwright, Stealth mode, and asynchronous API requests.

---

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

### 7. Wildberries API Scraper (iPhone 17 Pro Max)
- Scrapes product data from Wildberries via internal API
- Extracts: product name, price, article
- Uses `requests` with cookies and headers to mimic real browser
- Includes data cleaning, sorting by price (ascending/descending)
- Exports data to Excel (`.xlsx`)
- Demonstrates reverse-engineering of internal API endpoints

### 8. Wildberries Interactive Parser
- Interactive Wildberries parser with user input
- Search query and product count are set via console
- Extracts: product name, article, price, brand, characteristics
- Uses internal Wildberries API with browser-like headers
- Saves data to Excel (`.xlsx`)
- Full logging of all steps
- Error handling for missing characteristics
- Ready for real-world freelance orders

### 9. Async Parser with aiohttp + SQLite

- Scrapes data from [JSONPlaceholder](https://jsonplaceholder.typicode.com) API
- Uses `aiohttp` for asynchronous HTTP requests
- Saves data to SQLite database (`posts.db`)
- Creates table with fields: `id`, `userId`, `title`, `body`
- Handles errors and logs progress
- Demonstrates clean separation of concerns (fetching → saving → logging)
- Ready for integration into larger data pipelines

**Technologies:** Python, aiohttp, asyncio, SQLite3, logging

### 10. Weather Parser (Gismeteo)

- Parses weather data from [Gismeteo](https://www.gismeteo.ru/)
- Interactive search: user enters a city name
- Displays list of matching cities with indices
- User selects a city by number
- Extracts and displays:
  - Current temperature
  - Wind speed (m/s)
  - Atmospheric pressure
- Uses Playwright Stealth + Fake User-Agent to avoid detection
- Handles errors gracefully (city not found, index out of range, missing data)

**Technologies:** Python, Playwright, Playwright Stealth, Fake-UserAgent, asyncio, logging

---

## 🛠️ Technologies Used

- Python 3.9+
- Playwright
- SQLite3
- Playwright Stealth
- aiohttp (asynchronous HTTP requests)
- Requests (synchronous HTTP)
- BeautifulSoup (optional)
- Pandas
- asyncio
- fake_useragent
- JSON
- Excel (openpyxl)

---

## 📦 Installation

```bash
pip install -r requirements.txt
playwright install
