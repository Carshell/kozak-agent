"""
Модуль перевірки Nginx (статус-сторінка або доступність).
Конфігурація з env: NGINX_STATUS_URL.
"""
from modules.base import BaseModule, CheckResult
import asyncio
from typing import Any
import httpx
from config import (
    get_nginx_urls,
    get_nginx_timeout)


def check_nginx() -> tuple[str, str, dict[str, Any]]:  
    urls = get_nginx_urls()
    timeout = get_nginx_timeout()
    for url in urls:

        try:
            r = httpx.get(url, timeout=timeout)

            if not r.status_code == 200:
                return "error", f"Помилка зєднання {r.status_code}", {"url":url}
            
            elif r.status_code == 200:
                return "ok", f"Зєднання успішне {r.status_code}", {"url":url}

        except httpx.RequestError as exc:
            
            return "error", "Помилка зєднання ", {"url":url,"method": exc.request.method, "error": str(exc), "error2": exc.__cause__}






class NginxModule(BaseModule):   
    name = "nginx"

    async def run(self) -> CheckResult:

        loop = asyncio.get_event_loop()
        status, message, details = await loop.run_in_executor(None, check_nginx)

        return CheckResult(
            module=self.name,
            status=status,
            message=message,
            details=details,
        )
