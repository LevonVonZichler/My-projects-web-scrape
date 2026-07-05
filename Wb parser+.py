import asyncio
import json
import random
import logging
from playwright.async_api import async_playwright
from playwright_stealth import Stealth


async def random_delay(min_sec=1, max_sec=3):
    await asyncio.sleep(random.uniform(min_sec, max_sec))


def clean_price(p):
    if not p:
        return 0
    digits = "".join(filter(str.isdigit, str(p)))
    return int(digits) if digits else 0


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('parser.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await Stealth().apply_stealth_async(page)

        await page.goto('https://www.wildberries.ru/catalog/0/search.aspx?search=calvin+klein')
        await random_delay(2, 4)
        await page.wait_for_selector('.product-card', timeout=15000)

        all_kelvin = []
        kels = await page.locator('.product-card').all()
        logging.info(f"Найдено карточек: {len(kels)}")

        for i, kel in enumerate(kels[:10], 1):
            try:
                await kel.scroll_into_view_if_needed()
                await random_delay(0.5, 1.5)

                title = await kel.locator('a.product-card__link').get_attribute('aria-label')
                price_text = await kel.locator('.price__lower-price').inner_text()
                price = clean_price(price_text)

                dely = await kel.locator('[data-helper="delivery-display"]').inner_text()

                href = await kel.locator('a.product-card__link').get_attribute('href')
                if href:
                    art = href.split('/catalog/')[1].split('/')[0]
                else:
                    art = 'Not found'

                all_kelvin.append({
                    'Name': title,
                    'Price': price,
                    'Del': dely,
                    'Link': href,
                    'Articul': art
                })
                logging.info(f'Product {i} parsed!')

            except Exception as e:
                logging.error(f'Product {i} not parsed! Error: {e}')

        await browser.close()

    with open('config.json', 'w', encoding='utf-8') as file:
        json.dump(all_kelvin, file, ensure_ascii=False, indent=4)

    logging.info(f'Saved to JSON. Total: {len(all_kelvin)} products')


if __name__ == '__main__':
    asyncio.run(main())