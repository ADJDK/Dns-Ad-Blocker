# DNS Ad Blocker

A Python-based DNS server that blocks advertisement and tracking domains using a configurable blocklist while forwarding legitimate DNS requests to Google's DNS server. The project also implements DNS caching with TTL, request logging, and real-time statistics to improve performance and provide insights into DNS traffic.

---

## Features

- DNS packet parsing using `dnslib`
- UDP socket-based DNS server
- Blocks advertisement and tracker domains
- Forwards allowed requests to Google DNS (8.8.8.8)
- DNS response caching with TTL (Time-To-Live)
- Request logging
- Real-time DNS statistics
- Configurable blocklist
- Modular project structure

---

## Project Structure

```text
dns-ad-blocker/
│
├── server.py          # Main DNS server
├── client.py          # DNS client for testing
├── config.py          # Configuration settings
├── blocklist.py       # Blocklist loader
├── cache.py           # DNS cache with TTL
├── logger.py          # Logging utility
├── stats.py           # Request statistics
├── blocklist.txt      # Blocked domains
├── requirements.txt   # Project dependencies
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3
- Socket Programming
- UDP Protocol
- DNS Protocol
- dnslib

---

## How It Works

1. The client sends a DNS request to the server.
2. The server checks whether the requested domain is present in the blocklist.
3. If the domain is blocked, the server returns `0.0.0.0`.
4. If the domain is not blocked, the server checks the local cache.
5. If a valid cached response exists, it is returned immediately.
6. Otherwise, the request is forwarded to Google's public DNS server (`8.8.8.8`).
7. The received response is cached and sent back to the client.
8. Statistics and logs are updated after every request.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/dns-ad-blocker.git
```

Move into the project directory:

```bash
cd dns-ad-blocker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the DNS server:

```bash
python server.py
```

In another terminal, run the client:

```bash
python client.py
```

---

## Example Output

### Allowed Request

```
Allowed: google.com
```

### Blocked Request

```
Blocked: doubleclick.net
```

### Cache Hit

```
Cache Hit: google.com
```

### Statistics

```
====== DNS Statistics ======
Total Requests : 10
Blocked        : 3
Allowed        : 7
Cache Hits     : 2
============================
```

---

## Future Improvements

- Web dashboard for monitoring DNS traffic
- Automatic blocklist updates
- Whitelist support
- Multi-threaded request handling
- AI-based malicious/ad domain detection
- System-wide DNS service integration

---

## Learning Outcomes

This project helped me gain practical experience with:

- Computer Networks
- DNS Protocol
- UDP Socket Programming
- Caching Techniques
- Logging
- Python Networking
- Modular Software Design

---

## License

This project is intended for educational purposes.
