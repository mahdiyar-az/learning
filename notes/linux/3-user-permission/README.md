# 👤 User, Group, and Permission Management

### `whoami` — Who Am I
**Description:** Displays the current logged-in username.  
**Example:**
```bash
whoami
```
---

### `chmod` — Change Mode
**Meaning:** **ch**ange file **mod**e bits  
**Description:** Changes file permissions (read/write/execute).  
**Examples:**
```bash
chmod +x script.sh
chmod 755 myfile
```
---

### `chown` — Change Owner
**Meaning:** **ch**ange **own**er  
**Description:** Changes file or directory owner and group.  
**Examples:**
```bash
chown user:user file.txt
sudo chown -R username:group folder/
```
---

### `lsattr` — List File Attributes
**Meaning:** **l**i**s**t **attr**ibute  
**Description:** displays the file attributes on a Linux filesystem that support extended attributes.  
**Examples:**
```bash
lsattr /etc/passwd
```
---

### `groups` — Show Groups
**Description:** Displays all groups a user belongs to.  
**Example:**
```bash
groups
```
---

### `id` — Display User ID Info
**Description:** Displays user ID (UID), group ID (GID), and groups.  
**Example:**
```bash
id
```
---