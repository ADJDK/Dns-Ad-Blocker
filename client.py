import socket
from dnslib import DNSRecord

server=("127.0.0.1",5300)


query=DNSRecord.question("doubleclick.net")


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto(query.pack(),server)

print("Sent")

response,_=sock.recvfrom(512)

reply=DNSRecord.parse(response)

print(reply)