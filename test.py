import asyncio
import asyncpg
import datetime

async def main():

    conn = await asyncpg.connect(user='postgres', password='qwert12345',
                                 database='postgres', host='127.0.0.1', port = 5431)
    print(conn)

asyncio.run(main())