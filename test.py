import asyncio
import asyncpg
import datetime

async def main():

    conn = await asyncpg.connect(user='postgres', password='qwert12345',
                                 database='postgres', host='127.0.0.1', port = 5431)
    
    conn = await conn.fetchrow("SELECT 1 AS is_alive")
    print(conn["is_alive"])

asyncio.run(main())