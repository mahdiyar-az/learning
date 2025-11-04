# 🧠 System Information and Hardware

### `uname -a` — Kernel and OS Info
**Meaning:** **u**nix **name**  
**Description:** Displays detailed system information including kernel version.  
**Example:**
```bash
uname -a
```
---

### `hostnamectl` — System Information
**Description:** Shows or changes the system hostname and related metadata.  
**Example:**
```bash
hostnamectl
```
---

### `df -h` — Disk Free
**Meaning:** **d**isk **f**ree  
**Description:** Displays filesystem disk space usage in human-readable format.  
**Example:**
```bash
df -h
```
---

### `du -sh *` — Disk Usage
**Meaning:** **d**isk **u**sage  
**Description:** Displays disk usage of files and directories.  
**Example:**
```bash
du -sh *
```
---

### `free -h` — Memory Usage
**Description:** Shows memory and swap usage in a readable format.  
**Example:**
```bash
free -h
```
---

### `lscpu` — CPU Info
**Description:** Displays information about the CPU architecture.  
**Example:**
```bash
lscpu
```
---

### `lsblk` — Block Devices
**Description:** Lists information about block devices like disks.  
**Example:**
```bash
lsblk
```
---

### `uptime` — System Uptime
**Description:** Shows how long the system has been running.  
**Example:**
```bash
uptime
```
---

### `dmesg` — Kernel Messages
**Description:** Prints or controls the kernel ring buffer.  
**Example:**
```bash
dmesg | less
```
---

---

## `lsmod`
**Meaning:** List Modules  
**Description:** Displays the status of loaded kernel modules.  
**Example:**
```bash
lsmod
```

---

## `lspci`
**Meaning:** List PCI Devices  
**Description:** Shows information about PCI buses and devices.  
**Example:**
```bash
lspci
```

---

## `lsusb`
**Meaning:** List USB Devices  
**Description:** Displays USB buses and connected devices.  
**Example:**
```bash
lsusb
```