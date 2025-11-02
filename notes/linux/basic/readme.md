# 🧩 Basic Linux Commands

This section covers the most **fundamental and frequently used Linux commands** — the ones you’ll use daily for navigation, viewing files, managing data, and understanding your system.

---

## 📁 Navigation & Directories

### `pwd` — Print Working Directory
**Meaning:** **p**rint **w**orking **d**irectory  
**Description:** Shows the current directory path.  
**Example:**
```bash
pwd
# Output: /home/username/Documents
```

---

### `ls` — List
**Meaning:** **l**i**s**t  
**Description:** Lists files and directories in the current directory.  
**Examples:**
```bash
ls          # list files
ls -l       # long format
ls -a       # include hidden files
ls -lh      # human-readable sizes
```

---

### `cd` — Change Directory
**Meaning:** **c**hange **d**irectory  
**Description:** Switches to another directory.  
**Examples:**
```bash
cd /home        # go to /home
cd ..           # go one level up
cd ~            # go to home directory
cd /            # go to root directory
```

---

### `mkdir` — Make Directory
**Meaning:** **m**ake **dir**ectory  
**Description:** Creates a new directory.  
**Examples:**
```bash
mkdir new_folder
mkdir -p parent/child/grandchild  # create nested folders
```

---

### `rmdir` — Remove Directory
**Meaning:** **r**emove **dir**ectory  
**Description:** Deletes an empty directory.  
**Example:**
```bash
rmdir old_folder
```

---

## 📄 File Management

### `rm` — Remove
**Meaning:** **r**e**m**ove  
**Description:** Deletes files or directories. ⚠️ Irreversible.  
**Examples:**
```bash
rm file.txt
rm -r folder/
rm -rf /path/to/folder/
```

---

### `cp` — Copy
**Meaning:** **c**o**p**y  
**Description:** Copies files or directories.  
**Examples:**
```bash
cp file.txt backup.txt
cp -r folder1/ folder2/
```

---

### `mv` — Move
**Meaning:** **m**o**v**e  
**Description:** Moves or renames files/directories.  
**Examples:**
```bash
mv oldname.txt newname.txt
mv file.txt /home/user/docs/
```

---

### `touch` — Create Empty File / Update Timestamp
**Description:** Creates an empty file or updates the last modified time of an existing file.  
**Example:**
```bash
touch notes.txt
```

---

### `cat` — Concatenate
**Meaning:** **cat** = **concatenate**  
**Description:** Displays content of files or concatenates multiple files.  
**Examples:**
```bash
cat file.txt
cat file1.txt file2.txt > combined.txt
```

---

### `less` — View Large Files One Page at a Time
**Description:** Opens a file for viewing (scroll up/down).  
**Example:**
```bash
less longfile.log
```
- Press `q` to quit, `↑/↓` or `PgUp/PgDn` to scroll.

---

### `head` — Show Beginning of File
**Description:** Shows the first 10 lines by default.  
**Examples:**
```bash
head file.txt
head -n 5 file.txt
```

---

### `tail` — Show End of File
**Description:** Shows the last 10 lines by default.  
**Examples:**
```bash
tail file.txt
tail -f log.txt  # follow file changes in real time
```

---

## 🔍 Searching & Viewing

### `find` — Search for Files
**Description:** Searches for files/directories by name, type, etc.  
**Examples:**
```bash
find /home -name "*.txt"
find . -type d -name "test"
```

---

### `grep` — Global Regular Expression Print
**Meaning:** **g**lobal **r**egular **e**xpression **p**rint  
**Description:** Searches for a keyword or pattern in files.  
**Examples:**
```bash
grep "error" log.txt
grep -i "warning" *.log
```

---

## 🧠 System & User Info

### `whoami` — Who Am I
**Description:** Displays the current logged-in username.  
**Example:**
```bash
whoami
```

---

### `date` — Show System Date and Time
**Description:** Displays or sets the system date/time.  
**Example:**
```bash
date
```

---

### `df` — Disk Free
**Description:** Shows disk space usage of file systems.  
**Example:**
```bash
df -h
```

---

### `du` — Disk Usage
**Description:** Shows space used by files and directories.  
**Example:**
```bash
du -sh *
```

---

## ⚙️ Permissions & Ownership

### `chmod` — Change Mode
**Meaning:** **ch**ange file **mod**e bits  
**Description:** Changes file permissions (read/write/execute).  
**Example:**
```bash
chmod +x script.sh
```

---

### `chown` — Change Owner
**Meaning:** **ch**ange **own**er  
**Description:** Changes file owner and group.  
**Example:**
```bash
chown user:user file.txt
```

---

## 💬 Terminal Utilities

### `echo` — Print Text or Variables
**Description:** Displays text or variable values.  
**Examples:**
```bash
echo "Hello, Linux!"
echo $HOME
```

---

### `man` — Manual Pages
**Meaning:** **man**ual  
**Description:** Displays the full manual for any command.  
**Example:**
```bash
man ls
```
- Press `q` to quit the manual viewer.

---

### `--help` — Quick Help
**Description:** Shows a brief help message for any command.  
**Example:**
```bash
ls --help
```

---

### `clear` — Clear Terminal
**Description:** Clears the terminal screen.  
**Example:**
```bash
clear
```

---

### `history` — Command History
**Description:** Displays a list of previously used commands.  
**Examples:**
```bash
history
!45  # rerun command number 45
```

---

### `exit` — Exit Terminal Session
**Description:** Closes the current terminal session.  
**Example:**
```bash
exit
```

---

## 🧾 Quick Summary Table

| Command | Meaning (Full Form) | Description |
|----------|--------------------|-------------|
| `pwd` | Print Working Directory | Show current directory |
| `ls` | List | List files and directories |
| `cd` | Change Directory | Move between directories |
| `mkdir` | Make Directory | Create a folder |
| `rmdir` | Remove Directory | Delete empty directory |
| `rm` | Remove | Delete file/directory |
| `cp` | Copy | Copy files/directories |
| `mv` | Move | Move or rename |
| `touch` | — | Create empty file |
| `cat` | Concatenate | Display file contents |
| `less` | — | Scroll through file content |
| `head` | — | Show first lines |
| `tail` | — | Show last lines |
| `find` | — | Search for files |
| `grep` | Global Regular Expression Print | Search text in files |
| `whoami` | — | Show current user |
| `date` | — | Display date/time |
| `df` | Disk Free | Show filesystem usage |
| `du` | Disk Usage | Show directory size |
| `chmod` | Change Mode | Change file permissions |
| `chown` | Change Owner | Change file owner |
| `echo` | — | Print text/variables |
| `man` | Manual | Open command manual |
| `--help` | — | Quick help for a command |
| `clear` | — | Clear terminal screen |
| `history` | — | Show command history |
| `exit` | — | Exit terminal |

---

⭐ **Tip:** Combine these commands with pipes (`|`) and redirections (`>`, `>>`) to unlock the real power of Linux!