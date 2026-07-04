import asyncio
from encodings import utf_8
import json
from playwright.async_api import async_playwright
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        all_quotes = []
        page_number = 1
        while True:
            await page.goto(f'https://quotes.toscrape.com/page/{page_number}/')

            quotes = await page.locator('.text').all_inner_texts()
            authors = await page.locator('.author').all_inner_texts()
            for i in range(len(quotes)):
                all_quotes.append({
                    'Quote': quotes[i],
                    'Author': authors[i]
                })
            print(f'Quotes find {len(quotes)}, All find: {len(all_quotes)}')
            next_button = await page.locator('.next a').count()
            if next_button == 0:
                print('Page not found. Parsing is over.')
                break
            else:
                await page.locator('.next a').click()
                page_number += 1
                await asyncio.sleep(1)
        await browser.close()
        with open ('config.json', 'w', encoding='utf-8') as file:
            json.dump(all_quotes, file, indent=4, ensure_ascii=False)
        print('Save')
if __name__ == '__main__':
    asyncio.run(main())
