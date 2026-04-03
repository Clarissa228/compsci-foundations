# Networking Basics

## The Big Idea

Networking is how computers communicate with each other. Every time you visit a website, send a message, or stream video — you're using a network. Understanding the basics makes you a much better programmer.

---

## What is a Network?

A **network** is a group of connected devices (computers, phones, servers) that can share data. The biggest network is the **Internet** — a global network of networks.

---

## IP Addresses

Every device on a network has an **IP address** — a unique identifier, like a home address.

- **IPv4**: `192.168.1.1` (four numbers 0–255, separated by dots)
- **IPv6**: `2001:0db8:85a3::8a2e:0370:7334` (newer, much larger address space)

Special addresses:
- `127.0.0.1` = **localhost** (your own computer)
- `192.168.x.x` = private network (your home/office LAN)

---

## DNS — Domain Name System

You type `google.com` — but computers use IP addresses. **DNS** translates human-readable names to IP addresses.

```
You type: google.com
     ↓
DNS lookup: "What's the IP for google.com?"
     ↓
Returns: 142.250.80.46
     ↓
Your computer connects to that IP
```

DNS is like the phonebook of the internet.

---

## The OSI Model (Simplified)

Networks are organized in **layers**, each handling a different concern:

| Layer | Name | What it does | Example |
|-------|------|-------------|---------|
| 7 | Application | What the user sees | HTTP, HTTPS, FTP |
| 4 | Transport | End-to-end communication | TCP, UDP |
| 3 | Network | Routing between networks | IP |
| 2 | Data Link | Between adjacent devices | Ethernet, Wi-Fi |
| 1 | Physical | Actual bits over a medium | Cables, radio waves |

As a programmer, you mostly work at **Layer 7 (Application)**.

---

## TCP vs UDP

**TCP (Transmission Control Protocol)**:
- Guarantees delivery and order
- Slower (has to confirm every packet)
- Use for: web pages, emails, file transfers

**UDP (User Datagram Protocol)**:
- Fire and forget — no guarantee
- Faster
- Use for: video streaming, gaming, DNS, live audio

---

## HTTP — How the Web Works

**HTTP (HyperText Transfer Protocol)** is the language web browsers and servers speak.

When you visit a website:
1. Browser looks up the IP via DNS
2. Browser sends an **HTTP GET request** to the server
3. Server responds with HTML, CSS, JavaScript
4. Browser renders the page

```
GET /index.html HTTP/1.1
Host: example.com

→ Response: 200 OK
  Content: <html>...</html>
```

**HTTPS** = HTTP + encryption (TLS). The `s` means your connection is secure — always check for it!

### HTTP Status Codes
- `200 OK` — success
- `404 Not Found` — page doesn't exist
- `500 Internal Server Error` — server crashed
- `301 Redirect` — page moved

---

## Ports

A **port** is a numbered channel on a device. Different services run on different ports:

| Port | Service |
|------|---------|
| 80 | HTTP |
| 443 | HTTPS |
| 22 | SSH |
| 25 | Email (SMTP) |
| 5432 | PostgreSQL |

When you connect to `http://example.com`, you're actually connecting to `example.com:80`.

---

## Python Networking Basics

```python
import requests  # pip install requests

# Make an HTTP GET request
response = requests.get("https://api.github.com")
print(response.status_code)   # 200
print(response.json())        # Parse JSON response

# Download a webpage
response = requests.get("https://example.com")
print(response.text)          # HTML content
```

---

## 📺 Watch These

1. **How the Internet Works** — CrashCourse Computer Science
   👉 [https://www.youtube.com/watch?v=AEaKrq3SpW8](https://www.youtube.com/watch?v=AEaKrq3SpW8)

2. **HTTP Explained** — Academind
   👉 [https://www.youtube.com/watch?v=iYM2zFP3Zn0](https://www.youtube.com/watch?v=iYM2zFP3Zn0)

3. **DNS Explained** — DNS Made Easy
   👉 [https://www.youtube.com/watch?v=72snZctFFtA](https://www.youtube.com/watch?v=72snZctFFtA)

---

## Key Takeaways

- Every device has an **IP address**; **DNS** maps domain names to IP addresses
- **TCP**: reliable, ordered — for web, email. **UDP**: fast, lossy — for video, games
- **HTTP** is how browsers and servers communicate — you'll use it constantly as a developer
- Ports route traffic to specific services on a server
- Python's `requests` library makes HTTP calls easy

---

*Next up → [Practice Questions](./questions.md)*
