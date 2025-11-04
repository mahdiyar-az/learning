# 🌐 Networking Commands

### `ping` — Test Connectivity
**Description:** Tests network connectivity with another host.  
**Example:**
```bash
ping google.com
```
---

### `wget` — Web Get
**Meaning:** **w**eb **get**  
**Description:** download a file with url  
**Example:**
```bash
wget https://example.com/file.zip
```
---

### `ip` — Network Configuration
**Description:** Displays or configures network interfaces and routes.  
**Examples:**
```bash
ip addr
ip route show
```
---

### `ifconfig` — Interface Configuration
**Description:** Displays or modifies network interfaces (deprecated, replaced by `ip`).    
**Example:**
```bash
ifconfig eth0
```
---

### `ssh` — Secure Shell Connection
**Meaning:** **S**ecure **Sh**ell Connection  
**Description:** log into remote systems securely using encryption   
**Example:**
```bash
ssh -p 2222 user@server.example.com
```
---

### `ssh-keygen` — Generate SSH Keys
**Meaning:** **SSH** **KEY** **generate**  
**Description:** Generates public and private SSH key pairs for passwordless authentication. Keys are stored in ~/.ssh/id_rsa (private) and ~/.ssh/id_rsa.pub (public).  
**Example:**
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
---

### `netstat` / `ss` — Network Statistics
**Description:** Shows network connections, routing tables, and port usage.  
**Example:**
```bash
ss -antpl
```
---

### `traceroute` — Trace Path
**Description:** Traces the route packets take to a destination.  
**Example:**
```bash
traceroute 8.8.8.8
```
---

### `dig` — DNS Lookup
**Description:** Queries DNS name servers for host information.  
**Example:**
```bash
dig example.com
```
---

### `host` — DNS Query
**Description:** Performs DNS lookups for names or IPs.  
**Example:**
```bash
host example.com
```
---

### `hostname` — Display Hostname
**Description:** Shows or sets the system hostname.  
**Examples:**
```bash
hostname
hostname -I
```
---
---

## .`htpasswd`
**Description:** Creates and updates user authentication files for HTTP Basic Authentication.  
**Example:**
```bash
htpasswd -c /etc/apache2/.htpasswd user1
```

---

## `nmap`
**Meaning:** Network Mapper  
**Description:** Scans networks and detects devices and open ports.  
**Example:**
```bash
nmap 192.168.1.1
```

---

## `openssl`
**Description:** Toolkit for SSL/TLS and cryptography.  
**Example:**
```bash
openssl genrsa -out private.key 2048
```

---