import asyncio
import random
from idlelib import browser
from re import search

import aiohttp
import sqlite3
import logging
import pandas as pd
import playwright_stealth
import playwright
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import fake_useragent


async def delay(min_sec=1, max_sec=3):
    await asyncio.sleep(random.uniform(min_sec, max_sec))



async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await Stealth().apply_stealth_async(page)

        await page.goto('https://www.gismeteo.ru/')

        await delay(1, 3)

        search_wait = await page.wait_for_selector('input.input.js-input')
        search_text = input('Search:')
        try:
            search = await page.locator('input.input.js-input').fill(search_text)
        except:
            print('City not found')
            await browser.close()

        await delay(2,3)

        all_city = await page.locator('li.group-city').all()

        num = 1

        for city in all_city:
            name = await city.locator('span.name').inner_text()
            print(f'{name} --- Index {num}')
            num += 1

        target = input('Which city would you like? -> ')
        target = int(target)
        target -= 1

        try:
            finish_target = await page.locator('li.group-city').nth(target).click()
        except:
            print('Index not found')

        await delay(2, 3)

        try:

            today = await page.locator('a.weathertab').nth(0).click()

            await delay(2,3)

            tem = await page.locator('temperature-value').nth(0).inner_text()

            print(f'Today now: {tem}')

            speed = await page.locator('speed-value').nth(0).inner_text()

            print(f'Speed wind/m.s: {speed}')

            dav = await page.locator('pressure-value').nth(0).inner_text()

            print(f'Dav: {dav}')

        except:
            print('Params not found')

        #SQLite3 saved
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather(
            City TEXT,
            Temperature TEXT,
            Wind_speed TEXT,
            Pressure TEXT
            )
        ''')
        cursor.execute('DELETE FROM weather')
        cursor.execute('''
            INSERT INTO weather (City, Temperature, Wind_speed, Pressure)
            VALUES(?,?,?,?)
        ''', (search_text, tem, speed, dav))
        conn.commit()
        conn.close()


    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())