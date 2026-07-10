import json
from idlelib.iomenu import encoding
from logging import INFO, StreamHandler, handlers
from wsgiref import headers
import time

import pandas as pd
import requests
from pip._internal.commands import search
from pip._internal.utils import logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.log', mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logging.info('<Start program>')
print(f"{'-'*10}WELCOME TO WB SEARCH{'-'*10}")
print('| Write your search |')
cookies = {
    'external-locale': 'ru',
    'cfidsw-wb': '2HsyJjyAsmoEMEdJfppKnzKow4LmHqUWXhA9cWLsvj6e0HUXwFsjbswKq/nZZG5JZvXsalTAM+YprlvvRmqouujoJ0HuSA2wSbhUcC7A3UX6mGy1R7pev/ZrVq4I8XnD2eykypUkq5tbTX9Wk1Ewqlr14lLcWJGh2zsP',
    '_wbauid': '8006047381776253364',
    '__zzatw-wb': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UqQGYeaEteIEpHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYgGH1tKFIKEmBBSnJvG382XRw5YxELGX46Y11GRzcVJHt1EmxkCh5MVAw7FmBtEU0oP0dWVVY0XS1BPA5dP0NvdC1wIlNgS18kdl5ON1ofFzQkKww4DV9CQXZlJS0tUikSGmIPR1draF1QQSRaDHF/TQl6MjAbRWYkZk1bJEZYVH4pIhZzXWcgR0BNRzM1N1p0K2EcFyURGFE/RmhOUy4vYgo4RxgvS0Blb2wpYhw5YxENIj91F1lGQTZcGkt1ZS8MOTprbCRSUUNLY3waCmsvGhh+cSVUCg5iQkV2eCUtMWYnfEspNR0RMl5XVTQ7Z0FUWA==rK4rWw==',
    '_cp': '1',
    'x_wbaas_token': '1.1000.5cd95d0e34884268ac9b0f70a8188df5.MTV8MzEuNTYuMTg4LjE1OXxNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ0LjAuMC4wIFNhZmFyaS81MzcuMzZ8MTc4MzgyMDE2NnxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3ODM2OTA1NjZ8MQ==.MEQCIHZ52jDqZKYd0FmVotkKYMhpCthKQxsN+nUlMkr9xvkyAiA5+vcWtQeK8i9mGClVTAENCXNpekeGf9Pus5bU8VAZDw==',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'deviceid': 'site_47484d5dab7c4dd19fc0f88afcbae9b7',
    'priority': 'u=1, i',
    'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=makbook',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-queryid': 'qid800604738177625336420260710035536',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '14.16.3',
    'x-userid': '0',
    # 'cookie': 'external-locale=ru; cfidsw-wb=2HsyJjyAsmoEMEdJfppKnzKow4LmHqUWXhA9cWLsvj6e0HUXwFsjbswKq/nZZG5JZvXsalTAM+YprlvvRmqouujoJ0HuSA2wSbhUcC7A3UX6mGy1R7pev/ZrVq4I8XnD2eykypUkq5tbTX9Wk1Ewqlr14lLcWJGh2zsP; _wbauid=8006047381776253364; __zzatw-wb=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UqQGYeaEteIEpHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYgGH1tKFIKEmBBSnJvG382XRw5YxELGX46Y11GRzcVJHt1EmxkCh5MVAw7FmBtEU0oP0dWVVY0XS1BPA5dP0NvdC1wIlNgS18kdl5ON1ofFzQkKww4DV9CQXZlJS0tUikSGmIPR1draF1QQSRaDHF/TQl6MjAbRWYkZk1bJEZYVH4pIhZzXWcgR0BNRzM1N1p0K2EcFyURGFE/RmhOUy4vYgo4RxgvS0Blb2wpYhw5YxENIj91F1lGQTZcGkt1ZS8MOTprbCRSUUNLY3waCmsvGhh+cSVUCg5iQkV2eCUtMWYnfEspNR0RMl5XVTQ7Z0FUWA==rK4rWw==; _cp=1; x_wbaas_token=1.1000.5cd95d0e34884268ac9b0f70a8188df5.MTV8MzEuNTYuMTg4LjE1OXxNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ0LjAuMC4wIFNhZmFyaS81MzcuMzZ8MTc4MzgyMDE2NnxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3ODM2OTA1NjZ8MQ==.MEQCIHZ52jDqZKYd0FmVotkKYMhpCthKQxsN+nUlMkr9xvkyAiA5+vcWtQeK8i9mGClVTAENCXNpekeGf9Pus5bU8VAZDw==',
}

Poisk = input('Search: ')
num = input('How products to parsing:')
num = int(num)
time.sleep(2)
logging.info('<Search accept, start parsing>')


params = {
    'ab_testing': 'false',
    'appType': '1',
    'curr': 'rub',
    'dest': '-1257786',
    'hide_dtype': '15',
    'hide_vflags': '4294967296',
    'inheritFilters': 'true',
    'lang': 'ru',
    'locale': 'ru',
    'q1': Poisk,
    'query': Poisk,
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '30',
    'suppressSpellcheck': 'false',
}

response = requests.get(
    'https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search',
    params=params,
    cookies=cookies,
    headers=headers,
)
data = response.json()

data_clear = []
price = 0

products = data.get('products', [])
for product in products[:num]:
    name1 = product.get('name')
    id = product.get('id')
    brand = product.get('brand')
    sizes = product.get('sizes', [])
    price_data = sizes[0].get('price', {})
    price = price_data.get('product', 0) / 100
    meta = product.get('meta', {})
    char_all = meta.get('characteristics', [])
    chars_list = []

    for char in char_all:
        name = char.get('name')
        values = char.get('values')
        if name and values:
            chars_list.append(f"{name}: {', '.join(values)}")

    chars_str = '; '.join(chars_list) if chars_list else 'Нет характеристик'
    data_clear.append({
        'Name': name1,
        'Articul': id,
        'Price': price,
        'Brand': brand,
        'Characteristics': chars_str
    })
df = pd.DataFrame(data_clear)
df.to_excel('Wb.xlsx', index=False, engine='openpyxl')
logging.info('<Parsing is over>')
print('Parsing is over! All data save to Excel! :)')