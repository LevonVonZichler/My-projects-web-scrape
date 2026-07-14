import asyncio
import aiohttp
import sqlite3
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Use url...')
url = 'https://jsonplaceholder.typicode.com/posts'

async def fetch_posts(session):
    async with session.get(url) as responce:
        if responce.status == 200:
            posts = await responce.json()
            logging.info('Get all posts...')
            return posts
        else:
            logging.error(f'Error {responce.status}!')
            return []


async def main():
    logging.info('Create a session...')
    async with aiohttp.ClientSession() as session:
        data = await fetch_posts(session)
        logging.info('Gathering...')
        if data:
            logging.info('Done! Save to SQLite...')
            conn = sqlite3.connect('posts.db')
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                userid INTEGER,
                title TEXT,
                body TEXT
                )
            ''')
            cursor.execute('DELETE FROM posts')
            for post in data:
                cursor.execute('''
                    INSERT INTO posts (id, userid, title, body)
                    VALUES (?,?,?,?)
                ''', (post['id'], post['userId'], post['title'], post['body']))
            logging.info('Saved! Parsing is over.')
            conn.commit()
            conn.close()

        else:
            logging.error('Data not found!')


if __name__ == '__main__':
    asyncio.run(main())