import asyncio
import aiohttp
import fake_useragent
import json

async def get_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    UserAg = fake_useragent.UserAgent().random
    headers = {'User-Agent': UserAg}


    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:
            if responce.status == 200:
                users = await responce.json()
                return users
            else:
                print('Error')
                return []


async def main():
    print('Load a users...')
    users = await get_users()
    data = []
    if users:
        for user in users[:5]:
            name = user.get('name')
            email = user.get('email')
            city = user.get('address', {}).get('city')
            print(f"👤 {name}")
            print(f"   📧 {email}")
            print(f"   🏠 {city}\n")
            data.append({
                'Name': name,
                'Email': email,
                'City': city
            })
    else:
        print('Data is False')
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("✅ Сохранено в users.json")


if __name__ == '__main__':
    asyncio.run(main())
