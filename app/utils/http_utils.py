import httpx

async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

