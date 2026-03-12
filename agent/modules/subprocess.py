"""
Модуль перевірки процесів.
Конфігурація з env: .
"""
from modules.base import BaseModule, CheckResult
import asyncio
import asyncpg
from typing import Any
import subprocess
from config import (
    get_subprocess_services
)


async def check_subprocess():
    servisec = get_subprocess_services()
    details = {}
    resolt = True
    for ser in servisec:
        result = subprocess.run(
                ["sudo","systemctl", "is-active", "--quiet", ser]
            )
        if result.returncode == 0:
            details[ser] = "active"
            
        elif result.returncode == 3:
            details[ser] = "inactive"
            resolt = False
        elif result.returncode == 4:
            details[ser] = "not found"
            resolt = False
        else:
            details[ser] = "ERROR"
            resolt = False


    message = "ok" if resolt else "error"
    
    return resolt, message, details

class SubprocessModule(BaseModule):
    name = "subprocess"

    async def run(self) -> CheckResult:
        # TODO: реалізувати підключення (asyncpg) та просту перевірку (SELECT 1)
        ok, message, details = await check_subprocess()
        status = "ok" if ok else "error"
        return CheckResult(
            module=self.name,
            status=status,
            message=message,
            details=details,
        )
