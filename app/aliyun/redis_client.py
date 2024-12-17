import aioredis
from app.config import settings

redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(f"redis://{settings.redis_host}:{settings.redis_port}")
    print("Redis initialized")

