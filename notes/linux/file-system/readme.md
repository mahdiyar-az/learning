# 🗂️ File System Commands in Linux

This section covers the essential Linux commands for **file system management** — including navigation, file operations, permissions, and disk management.

---

## 📁 1. Navigation Commands

| Command | Meaning | Description |
|----------|----------|-------------|
| `pwd` | **Print Working Directory** | Displays the current directory path. |
| `cd` | **Change Directory** | Moves between directories (e.g., `cd /home`, `cd ..`, `cd ~`). |
| `ls` | **List** | Lists files and directories (`ls -l`, `ls -a`, `ls -lh`). |
| `tree` | — | Shows directory structure in a tree-like format. |

---

## 📄 2. File and Directory Operations

| Command | Meaning | Description |
|----------|----------|-------------|
| `touch` | — | Creates an empty file or updates its timestamp. |
| `cat` | **Concatenate** | Displays or joins file contents (`cat file1 file2`). |
| `cp` | **Copy** | Copies files or directories (`cp file1 file2`, `cp -r dir1 dir2`). |
| `mv` | **Move** | Moves or renames files (`mv file1 newname`). |
| `rm` | **Remove** | Deletes files (`rm file.txt`, `rm -r folder/`). |
| `mkdir` | **Make Directory** | Creates a new folder (`mkdir mydir`). |
| `rmdir` | **Remove Directory** | Deletes an empty directory. |

---

## 🔍 3. Viewing and Searching Files

| Command | Meaning | Description |
|----------|----------|-------------|
| `head` | — | Shows the first 10 lines of a file (`head -n 5 file.txt`). |
| `tail` | — | Shows the last 10 lines of a file (`tail -f logfile.log`). |
| `less` | — | Opens a file in a scrollable viewer. |
| `grep` | **Global Regular Expression Print** | Searches for patterns in files (`grep "word" file.txt`). |
| `find` | — | Searches for files (`find /home -name "*.txt"`). |
| `locate` | — | Quickly finds files by name using a pre-built index. |

---

## 🔐 4. File Permissions and Ownership

| Command | Meaning | Description |
|----------|----------|-------------|
| `chmod` | **Change Mode** | Modifies file permissions (`chmod 755 file.sh`). |
| `chown` | **Change Owner** | Changes file ownership (`chown user:group file`). |
| `umask` | **User Mask** | Sets default permission mask for new files. |
| `ls -l` | — | Displays file permissions and ownership info. |

---

## 💽 5. Disk and Storage Management

| Command | Meaning | Description |
|----------|----------|-------------|
| `df` | **Disk Free** | Displays disk usage by filesystem. |
| `du` | **Disk Usage** | Shows directory or file space usage (`du -sh folder/`). |
| `mount` | — | Mounts a filesystem (`mount /dev/sda1 /mnt`). |
| `umount` | — | Unmounts a filesystem (`umount /mnt`). |
| `fdisk` | — | Used for disk partitioning. |
| `lsblk` | **List Block Devices** | Lists information about disks and partitions. |
| `blkid` | **Block ID** | Shows UUID and type info for storage devices. |

---

## 🧰 6. Links

| Command | Meaning | Description |
|----------|----------|-------------|
| `ln` | **Link** | Creates a hard link (`ln file1 link1`). |
| `ln -s` | **Symbolic Link** | Creates a soft (symbolic) link (`ln -s target link`). |

---

## 🧾 Summary

| Category | Commands |
|-----------|-----------|
| Navigation | `pwd`, `cd`, `ls`, `tree` |
| File Ops | `touch`, `cat`, `cp`, `mv`, `rm`, `mkdir`, `rmdir` |
| Viewing & Search | `head`, `tail`, `less`, `grep`, `find`, `locate` |
| Permissions | `chmod`, `chown`, `umask`, `ls -l` |
| Disk Mgmt | `df`, `du`, `mount`, `umount`, `fdisk`, `lsblk`, `blkid` |
| Links | `ln`, `ln -s` |

---

📘 **Tip:** Use `man <command>` or `<command> --help` to view detailed documentation for any command.
