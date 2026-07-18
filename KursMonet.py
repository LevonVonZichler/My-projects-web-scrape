import asyncio
import random
import sqlite3
import logging
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def delay(min_sec=1, max_sec=3):
    await asyncio.sleep(random.uniform(min_sec, max_sec))



async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        logging.info('Browser is open')
        await Stealth().apply_stealth_async(page)
        logging.info('Stealth mode asctivited!')
        await page.goto('https://xn----dtbfdbwspgnceulm.xn--p1ai/chart-online.php')

        await delay(2,3)
        text_wait = await page.wait_for_selector('td.val')
        texts = await page.locator('td.val').all()
        num = 1
        conn = sqlite3.connect('Kurs.db')
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS kurs
                       (
                           Title TEXT,
                           Cost TEXT,
                           Rost TEXT
                       )
                       ''')
        for text in texts:
            try:
                value = await text.locator('span.value.spred_up').inner_text()
                logging.info(f'Value is {num} find')
                title = await text.locator('span.help').inner_text()
                logging.info(f'Title is {num} find')
                rost = await text.locator('span.vall.spred_up').inner_text()
                logging.info(f'Rost is {num} find')
                clear_rost =  rost.strip('()')
                rost_number = clear_rost.strip('+')
                rost_number = float(rost_number)
                cursor.execute('''
                               INSERT INTO kurs (Title, Cost, Rost)
                               VALUES (?, ?, ?)
                               ''', (title, value, clear_rost))
            except Exception as e:
                logging.error(f'Error: {e}')
                value = None
                title = None
                rost = None
                continue
            num += 1
        conn.commit()
        conn.close()

    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())