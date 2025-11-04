# ⚙️ Process and Service Management

### `ps` — Process Status
**Meaning:** **p**rocess **s**tatus  
**Description:** Lists currently running processes.  
**Examples:**
```bash
ps
ps aux
```
---

### `crontab` — Schedule Recurring Tasks
**Meaning:** **cron** **tab**le    
**Description:** chedule tasks to run automatically at specific times     
**Examples:**
```bash
crontab -e
```
---

### `pidof` — Process ID Of
**Meaning:** **p**rocess **ID** **OF** 
**Description:** displays the Process ID of a running program by its name.
**Examples:**
```bash
pidof chrome
```
---

### `top` — Task Manager
**Description:** Displays real-time running processes.  
**Example:**
```bash
top
```
---

### `htop` — Interactive Process Viewer
**Description:** An improved version of `top` with a color interface.  
**Example:**
```bash
htop
```
---

### `kill` — Terminate Process
**Description:** Sends a signal to terminate a process by PID.  
**Example:**
```bash
kill 1234
```
---

### `killall` — Kill by Name
**Description:** Kills all processes by name.  
**Example:**
```bash
killall firefox
```
---

### `systemctl` — Control System Services
**Description:** Manages systemd services.  
**Examples:**
```bash
systemctl start nginx
systemctl status apache2
systemctl stop apache2
systemctl enable apache2
systemctl disable apache2
systemctl mask apache2
systemctl unmask apache2


```
---
### `journalctl` — Query and View System Logs
**Description:** journalctl displays and queries logs collected by systemd-journald, the central logging service in most  
**Examples:**
```bash
journalctl
```
---
### `service` — Manage Services
**Description:** Starts, stops, or restarts system services.  
**Examples:**
```bash
service ssh start
service apache2 restart
```
---

### `nice` — Set Process Priority
**Description:** Starts a process with a defined priority.  
**Example:**
```bash
nice -n 10 process_name
```
---

### `renice` — Change Priority
**Description:** Changes the priority of a running process.  
**Example:**
```bash
renice 5 -p 1234
```
---

### `jobs` — List Background Jobs
**Description:** Shows jobs running in the background.  
**Example:**
```bash
jobs
```
---

### `fg` / `bg` — Foreground / Background
**Description:** Moves background jobs to foreground or vice versa.  
**Examples:**
```bash
fg 1
bg 1
```
---