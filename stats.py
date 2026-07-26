stats = {
    "total_requests": 0,
    "blocked_requests": 0,
    "allowed_requests": 0,
    "cache_hits": 0
}


def print_stats():
    print("\n====== DNS Statistics ======")
    print(f"Total Requests : {stats['total_requests']}")
    print(f"Blocked        : {stats['blocked_requests']}")
    print(f"Allowed        : {stats['allowed_requests']}")
    print(f"Cache Hits     : {stats['cache_hits']}")
    print("============================\n")