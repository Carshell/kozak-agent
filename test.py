import httpx

r = httpx.get('https://www.google.com/?hl=uk', timeout=5)

print(r.status_code)