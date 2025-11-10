# 📁 File and Directory Management

### `pwd` — Print Working Directory
**Meaning:** **p**rint **w**orking **d**irectory  
**Description:** Displays the full path of the current working directory.  
**Example:**
```bash
pwd
# Output: /home/user
```
---

### `ls` — List
**Meaning:** **l**i**s**t  
**Description:** Lists files and directories in the current directory.  
**Examples:**
```bash
ls
ls -l
ls -a
ls -lh
```
---

### `cd` — Change Directory
**Meaning:** **c**hange **d**irectory  
**Description:** Changes the current working directory.  
**Examples:**
```bash
cd /home
cd ..
cd ~
cd /
```
---

### `mkdir` — Make Directory
**Meaning:** **m**ake **dir**ectory  
**Description:** Creates a new directory.  
**Examples:**
```bash
mkdir new_folder
mkdir -p parent/child/grandchild
```
---

### `rmdir` — Remove Directory
**Meaning:** **r**emove **dir**ectory  
**Description:** Removes an empty directory.  
**Example:**
```bash
rmdir old_folder
```
---

### `rm` — Remove
**Meaning:** **r**e**m**ove  
**Description:** Deletes files or directories. ⚠️ This action is irreversible.  
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
**Description:** Creates an empty file or updates the timestamp of an existing file.  
**Example:**
```bash
touch notes.txt
```
---

### `cat` — Concatenate
**Meaning:** **cat** = **concatenate**  
**Description:** Displays file content or concatenates multiple files.  
**Examples:**
```bash
cat file.txt
cat file1.txt file2.txt > combined.txt
```
---

## `wc` — Word Count
**Meaning:** Word Count  
**Description:** Displays the number of lines, words, and bytes in a file.  
**Example:**
```bash
wc filename.txt
wc -l filename.txt  # Count lines only
```

---

## `find`
**Description:** Searches for files and directories in a directory hierarchy.  
**Example:**
```bash
find /home -name "*.txt"
```

---

## `>`  `>>`
**Description:** Used for redirection.
- `>` overwrites a file.
- `>>` appends to a file.  
  **Example:**
```bash
echo "Hello" > file.txt
echo "World" >> file.txt
```

---

## `vmstat` — Virtual Memory Statistics
**Meaning:** Virtual Memory Statistics  
**Description:** Displays information about system processes, memory, paging, block I/O, and CPU.  
**Example:**
```bash
vmstat 2 5  # Refresh every 2 seconds, 5 times
```

---
### `sed` 
**Meaning:** 
**Description:**  
**Examples:**
```bash

```
---

### `less` — View Large Files
**Description:** Opens a file for viewing one screen at a time.  
**Example:**
```bash
less longfile.log
```
- Press `q` to quit.  
---

### `head` — Show Beginning of File
**Description:** Displays the first 10 lines by default.  
**Examples:**
```bash
head file.txt
head -n 5 file.txt
```
---

### `tail` — Show End of File
**Description:** Displays the last 10 lines by default.  
**Examples:**
```bash
tail file.txt
tail -f log.txt
```
---

### `find` — Search for Files
**Description:** Searches for files or directories by name, type, or other attributes.  
**Examples:**
```bash
find /home -name "*.txt"
find . -type d -name "test"
```
---

### `mount` — attach or mount a filesystem
**Description:** attach a filesystem, external drive to a specific directory in the Linux filesystem tree
**Examples:**
```bash
mount /dev/sdb1 /mnt/usb
mount -t ext4 /dev/sda2 /media/data
```
---

### `unmount` — un-mount
**Description:** Used to safely detach (unmount) a filesystem or device from the Linux directory tree. This ensures that all data is written and no corruption occurs.  
**Examples:**
```bash
umount /mnt/usb
umount /dev/sdb1
```
---


## `iotop`
**Description:** Displays disk I/O usage by processes.  
**Example:**
```bash
sudo iotop
```

---

##  `tar`
**Meaning:** Tape Archive  
**Description:** Archives multiple files into one and can compress them.  
**Example:**
```bash
tar -cvf archive.tar files/
tar -xvf archive.tar
```

---

## `dd`
**Description:** Converts and copies files, often used for disk cloning.  
**Example:**
```bash
sudo dd if=/dev/sda of=/dev/sdb bs=4M status=progress
```

---

## `file`
**Description:** Determines the file type.  
**Example:**
```bash
file document.pdf
```

---

## `watch`
**Description:** Runs a command periodically and displays output.  
**Example:**
```bash
watch -n 2 df -h
```

---

## `which`
**Description:** Shows the full path of a command.  
**Example:**
```bash
which python3
```

---

## `whatis`
**Description:** Displays a short description of a command.  
**Example:**
```bash
whatis ls
```

---

## `whereis`
**Description:** Locates the binary, source, and manual page of a command.  
**Example:**
```bash
whereis gcc
```

---

## `info`
**Description:** Shows detailed documentation about a command.  
**Example:**
```bash
info grep
```

---

##  `uname`
**Meaning:** Unix Name  
**Description:** Displays system information.  
**Example:**
```bash
uname -a
```

---

##  `echo`
**Description:** Prints text or variables to the terminal.  
**Example:**
```bash
echo "Hello World"
echo $HOME
```
---
##  `env`
**Meaning:** Environment  
**Description:** Displays environment variables.  
**Example:**
```bash
env
```

---

## `export`
**Description:** Sets environment variables for the current session.  
**Example:**
```bash
export PATH=$PATH:/usr/local/bin
```

---

## `tee`
**Description:** Reads from standard input and writes to both standard output and a file.  
**Example:**
```bash
ls | tee output.txt
```

---

## `xargs`
**Description:** Builds and executes command lines from standard input.  
**Example:**
```bash
find . -name "*.log" | xargs rm
```

---

## `ulimit`
**Description:** Controls user resource limits.  
**Example:**
```bash
ulimit -n 1024  # Limit open files
```

---

## `chroot`
**Meaning:** Change Root  
**Description:** Runs a command or shell with a different root directory.  
**Example:**
```bash
sudo chroot /mnt/new_root /bin/bash
```
