import time
from config import CACHE_TTL

cache={}

def get_cached(domain):
    if domain in cache:
        response,expiry=cache[domain]

        if time.time() < expiry:
            return response

        del cache[domain]

    return None

def add_cache(domain,response):
    cache[domain]=(response, time.time() + CACHE_TTL)