import asyncio
import json
import random
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import logging



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('parser.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)



def clean_price(p):
    if not p:
        return 0
    digits = "".join(filter(str.isdigit, str(p)))
    return int(digits) if digits else 0



async def random_delay(min_sec=1,max_sec=3):
    await asyncio.sleep(random.uniform(min_sec,max_sec))


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        logging.info('Browser is start')

        await Stealth().apply_stealth_async(page)


        all_products = []
        num = 1

        await page.goto('https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D1%8B')
        logging.info('Page opened')
        await random_delay(1, 2)
        await page.wait_for_selector('.product-card-list .product-card')
        phones = await page.locator('.product-card-list .product-card').all()
        for phone in phones[:10]:
            try:
                await phone.scroll_into_view_if_needed()
                await random_delay(1, 2)
                link = phone.locator('a.product-card__link')
                title = await link.get_attribute('aria-label')
                price_text = await phone.locator('.price__lower-price').inner_text()
                price = clean_price(price_text)
                all_products.append({
                    'Name': title,
                    'Price': price
                })
                logging.info(f'Cicle {num} is over')
                num += 1
            except Exception:
                logging.error('Get a error! Go to next phones...')
                continue
        logging.info('Parsing is over.')

    await browser.close()
    logging.info('Browser is close')

    all_products = [p for p in all_products if p['Price'] > 0]
    all_products.sort(key=lambda x: x['Price'])

    with open('wb_products.json', 'w', encoding='utf-8') as file:
        json.dump(all_products, file, ensure_ascii=False, indent=4)
    logging.info('Saved')
if __name__ == '__main__':
    asyncio.run(main())
