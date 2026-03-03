"""
Модуль перевірки зʼєднання з PostgreSQL.
Конфігурація з env: POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.
"""
from modules.base import BaseModule, CheckResult
import asyncio
import asyncpg
from typing import Any
from config import (
    get_postgres_host,
    get_postgres_port,
    get_postgres_user,  
    get_postgres_password,
    get_postgres_db,
)
import asyncpg

async def check_postgress_db():
    host2 = get_postgres_host()
    port2 = get_postgres_port()
    user2 = get_postgres_user()
    password2 = get_postgres_password()
    db2 = get_postgres_db()

    details = {"user":user2, "port":port2, "host": host2, "password": password2, "db":db2}

    try:
        conn = await asyncpg.connect(user=user2, password=password2,
                                 database=db2, host=host2, port = port2)
        
        row = await conn.fetchrow('SELECT * FROM users WHERE name = $1', 'Bob')

        if row:
            return True, "DB works", details
        else:
            return False, "Db didn't return anything", details
        
    except Exception as e:
        return False, f"{e}", details

class PostgresModule(BaseModule):
    name = "postgres"

    async def run(self) -> CheckResult:
        # TODO: реалізувати підключення (asyncpg) та просту перевірку (SELECT 1)
        ok, message, details = await check_postgress_db()
        status = "ok" if ok else "error"
        return CheckResult(
            module=self.name,
            status=status,
            message=message,
            details=details,
        )
