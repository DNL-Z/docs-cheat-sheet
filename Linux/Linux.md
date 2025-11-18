# 🐧 Linux Shell

Command-line interface and shell utilities for Linux operating systems, including file management, SSH, compression, permissions, and scripting.

## 📑 Table of Contents

- [📂 File System Basics](#-file-system-basics)
  - [Navigation](#navigation)
  - [File Operations](#file-operations)
  - [Directory Operations](#directory-operations)
  - [File Search and Filtering](#file-search-and-filtering)
- [🔐 SSH (Secure Shell)](#-ssh-secure-shell)
  - [Connect to SSH](#connect-to-ssh)
- [📦 SCP (Secure Copy Protocol)](#-scp-secure-copy-protocol)
  - [Transfer Files](#transfer-files)
- [🗜️ Compression & Decompression](#-compression--decompression)
  - [Decompress Files](#decompress-files)
  - [Compress Files](#compress-files)
- [🔑 Access Permissions](#-access-permissions)
  - [Permission Values](#permission-values)
  - [Changing Permissions](#changing-permissions)
  - [Changing Ownership](#changing-ownership)
- [📜 Scripts](#-scripts)
  - [Script Execution](#script-execution)
  - [Script Permissions](#script-permissions)
  - [Comparison Operators](#comparison-operators)
- [🛠️ Advanced Commands](#-advanced-commands)
  - [Text Processing](#text-processing)
  - [Log Analysis](#log-analysis)
  - [Pattern Matching](#pattern-matching)

---

## 📂 File System Basics

### Navigation

**Return to the user home directory or root directory**

```bash
  cd ~
  cd /
```

**Show the current path**

```bash
  pwd
```

### File Operations

**List all processes (process status)**

```bash
  ps
```

**List files including hidden files**

```bash
  ls -la
  tree -d
  tree -I 'node_modules'
```

**Create an empty file**

```bash
  touch <file_name>
```

**Write or create content in a file**

```bash
  nano <file_name>
```

**Copy files or directories**

```bash
  cp <source> <directory>
```

**Rename or move a file or folder**

```bash
  mv <source> <directory>
```

**Create hard links and symbolic links**

```bash
  ln <source> <directory>
```

**Delete a file**

```bash
  rm <file_or_directory>
```

### Directory Operations

**Create an empty directory**

```bash
  mkdir <folder_name>
```

**Create nested directory structure**

```bash
  mkdir -p 1/3/6/2/6/8
```

**Create a directory in the user's home directory**

```bash
  mkdir ~root/temporary_directory
```

**Delete an empty directory**

```bash
  rmdir /tmp/<directory_name>
```

**Delete a directory and all its contents recursively**

(remove directories and their contents recursively: -r, -R, --recursive)

```bash
  rm -r /tmp/<folder_name>
```

### File Search and Filtering

**Find a file**

```bash
  find / -name <file_name> (-print)
```

**List directories /etc and /bin**

```bash
  ls /etc /bin
```

**List content and redirect to the file**

```bash
  ls /etc > tmp/configurations.log
```

**List files starting with uppercase letter in /etc**

```bash
  ls /etc/[A-Z]*
  ls /etc | grep [A-Z]*
```

**List files containing a digit**

```bash
  ls /var/log | grep [0-9]
  ls /var/log/*[0-9]*
```

**Common text processing commands:**

- **sort** : sort lines of text files
- **grep** : print lines matching a pattern
- **cut** : remove sections from each line of files

---

## 🔐 SSH (Secure Shell)

### Connect to SSH

**Basic SSH connection**

```bash
  ssh user@ip_address
```

**SSH connection with a specific key**

```bash
  ssh -i ~/.ssh/id_rsa_prod user@ip_address
```

**Generate SSH RSA key**

```bash
  ssh-keygen -t rsa -b 1024 -f ~/.ssh/id_rsa_eval -N protected
```

---

## 📦 SCP (Secure Copy Protocol)

### Transfer Files

**Transfer/Download a remote directory to local (-r for recursive, i.e., entire folder)**

```bash
  scp -r user@server.com:/path/of/external/folder /path/of/local/folder
```

**Transfer/Upload a local directory to remote**

```bash
  scp -r /local/folder user@ip_address:/remote/folder
```

---

## 🗜️ Compression & Decompression

### Decompress Files

**Decompress a BZ2 file**

```bash
  bzcat access.log.bz2
```

**Decompress a GZIP file**

```bash
  gzip access.log.gz
```

**Decompress a TGZ file**

```bash
  tar xzvf <archive_name>.tar.gz
```

### Compress Files

**Compress to TAR.GZ**

```bash
  tar czvf <archive_name>.tar.gz <directory_name>
```

---

## 🔑 Access Permissions

### Permission Values

```
r: read permission = 4
w: write permission = 2
x: execute permission = 1
```

### Changing Permissions

**Change file permissions**

```bash
  chmod 117 file.txt
```

**Make a script executable**

```bash
  chmod +x <script.sh>
```

**Grant execution right to user for script.sh**

```bash
  chmod u+x script.sh
```

**Change script permissions for multiple users**

```bash
  chmod u+x,g+x,o-x script.sh
```

**Recursively change permissions**

```bash
  sudo chmod -R 775 /folder_name
```

### Changing Ownership

**Change group to "ubuntu" for all files in the /src directory**

```bash
  chown :ubuntu ~/src
```

**Change owner and group**

```bash
  sudo chown -R owner:group /folder_name
```

---

## 📜 Scripts

### Script Execution

**Execute a script**

```bash
  ./<script.sh>
```

**Debug script execution**

```bash
  bash -x <script.sh>
```

### Script Permissions

**Grant execution permission to the user for script.sh**

```bash
  chmod u+x script.sh
```

**Modify script permissions**

```bash
  chmod u+x,g+x,o-x script.sh
```

### Comparison Operators

**Mathematical operators for scripts**

```
-lt  =>  <   (less than)
-le  =>  <=  (less than or equal)
-gt  =>  >   (greater than)
-ge  =>  >=  (greater than or equal)
-eq  =>  =   (equal)
```

---

## 🛠️ Advanced Commands

### Text Processing

**Display the first 100 lines of a file**

```bash
  bzcat listing.csv.bz2 | head -100
  bzcat listing.csv.bz2 | head -n 100
```

**Top 100 ascending count of unique occurrences from the 6th field**

```bash
  cut -f 6 nasa.tsv | sort | uniq -c | sort | tail -n 5
```

**Count occurrences of each unique creation date and time in /dev directory**

```bash
  ls -l /dev | cut -c 36-47 | sort | uniq -c
```

### Log Analysis

**Top 5 articles from the log file**

```bash
  cat 01-Oct.log | cut -d " " -f 7 | grep article | sort | uniq -c | sort -n | tail -n 5
```

### Pattern Matching

**Sort files with pattern matching**

```bash
  ls -l a* b* c*
  # Equivalent to:
  ls -l [abc]*

  # Complex pattern matching
  ls -l fi??[^l]*
  # Equivalent to:
  ls -l fi[cl][he][^l]*
```
