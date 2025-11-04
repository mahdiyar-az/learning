# 📦 Package Management

### `apt update` — Update Package Index
**Description:** Updates the list of available packages (/etc/apt/sources.list).  
**Example:**
```bash
sudo apt update
```
---

### `apt upgrade` — Upgrade Packages
**Description:** Upgrades all upgradable packages.  
**Example:**
```bash
sudo apt upgrade
```
---

### `apt install` — Install Package
**Description:** Installs a new software package.  
**Example:**
```bash
sudo apt install nginx
```
---

### `apt remove` — Remove Package
**Description:** Removes a package from the system.  
**Example:**
```bash
sudo apt remove nginx
```
---

### `rpm -qa` — List Installed Packages
**Description:** Lists all installed RPM packages.  
**Example:**
```bash
rpm -qa
```
---

### `dpkg -l` — List Installed DEB Packages
**Meaning:** **d**eb **pac**kag  
**Description:** Lists installed packages on Debian systems.  
**Example:**
```bash
dpkg -l
```
---

### `apt proxy` — set proxy for installation

**Description:** locate here /etc/apt/apt.conf 

```
Acquire::http::Proxy "http://192.168.1.10:8080/";
Acquire::http::Proxy::archive.ubuntu.com "DIRECT";
```

