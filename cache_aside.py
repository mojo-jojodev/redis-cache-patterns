import json
from redis import Redis

def cache_aside(r: Redis, key: str, ttl: int, loader):
    cached = r.get(key)
    if cached is not None:
        return json.loads(cached)
    value = loader()
    r.set(key, json.dumps(value), ex=ttl)
    return value
