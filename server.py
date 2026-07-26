import socket
from dnslib import DNSRecord,RR, A
from logger import log_request
from blocklist import load_blocklist
from config import SERVER_HOST, SERVER_PORT, UPSTREAM_DNS, BLOCK_IP
from cache import get_cached,add_cache
from stats import stats, print_stats



server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((SERVER_HOST, SERVER_PORT))

google_dns=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("DNS server listing on 127.0.0.1:5300")

blocked=load_blocklist()

while True:
    data,addr=server.recvfrom(512)
    stats["total_requests"] += 1

    request=DNSRecord.parse(data)

    domain=str(request.q.qname).rstrip(".")
  
    

    is_blocked=False

    for blocked_domain in blocked:
        if domain.endswith(blocked_domain):
            is_blocked=True
            break
    
    if is_blocked:
        stats["blocked_requests"] += 1
        print("Blocked: ",domain)
        log_request("BLOCKED",domain)
        reply=request.reply()
        reply.add_answer(RR(domain,rdata=A(BLOCK_IP)))

        server.sendto(reply.pack(),addr)

        print_stats()

    else:

        cached_response= get_cached(domain)

        if cached_response:
            stats["cache_hits"] += 1
            stats["allowed_requests"] += 1
            print("Cache Hit", domain)
            server.sendto(cached_response,addr)
            print_stats()
            continue

        
        print("Allowed: ",domain)

        print("ALLOWED: ",domain)

        google_dns.sendto(data,UPSTREAM_DNS)
        

        response,_=google_dns.recvfrom(512)
        stats["allowed_requests"] += 1

        add_cache(domain,response)

        server.sendto(response,addr)

        print_stats()