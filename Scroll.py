import asyncio
import random
import fake_useragent
from fake_useragent import UserAgent
from playwright.async_api import async_playwright
import json
import pandas as pd
from fake_useragent import UserAgent

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('http://quotes.toscrape.com/scroll')

        all_books = []
        previous_c = 0
        max_scroll = 20

        for _ in range(max_scroll):
            quote = await page.wait_for_selector('.quote')
            current_q = await page.locator('.quote').all()
            current_c = len(current_q)
            if current_c == previous_c:
                break
            previous_c = current_c
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(1500)
        all_quotes_elem = await page.locator('.quote').all()
        for elem_q in all_quotes_elem:
            text = await elem_q.locator('.text').inner_text()
            author = await elem_q.locator('.author').inner_text()
            tags = await elem_q.locator('.tags').inner_text()
            all_books.append({
                'Text': text,
                'Author': author,
                'Tags': tags
            })
        await browser.close()

        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(all_books, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    asyncio.run(main())
