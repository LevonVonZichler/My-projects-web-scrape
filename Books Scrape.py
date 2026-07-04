import asyncio
import json
import random
from itertools import count
import pandas
import pandas as pd

from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import logging


#Logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('parser.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


#Replay
async def replay_zone(min_sec=1, max_sec=3):
    await asyncio.sleep(random.uniform(min_sec, max_sec))



async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await Stealth().apply_stealth_async(page)
        i = 1
        await page.goto(f'https://books.toscrape.com/catalogue/page-{i}.html')


        all_books = []


        books_wait = await page.wait_for_selector('.product_pod')
        books = await page.locator('.product_pod').all()

        while True:
            for book in books:
                try:
                    title = await book.locator('h3 a').get_attribute('title')
                    price = await book.locator('.price_color').inner_text()
                    stock = await book.locator('.instock').inner_text()
                    href = await book.locator('.image_container a').get_attribute('href')
                    full_link = f'https://books.toscrape.com/catalogue/{href}'
                    await page.goto(full_link)
                    decr = await page.locator('p').nth(3).inner_text()
                    await page.go_back()
                    next3 = page.get_by_text('next').count()
                    if next3 == 0:
                        break
                except Exception:
                    logging.error('Book no found. next...')
                    continue
            await page.get_by_text('next').click()

            all_books.append({
                'Name': title,
                'Price': price,
                'Stock': stock,
                'Decr': decr[:200]
            })
            await browser.close()
            df = pd.DataFrame(all_books)
            df.to_csv('books.csv')

if __name__ == '__main__':
    asyncio.run(main())
