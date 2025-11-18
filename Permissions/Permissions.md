# 🔑 File Permissions

Command-line utilities for managing file and directory permissions in Unix-based systems, including access rights modification and ownership management.

## 📑 Table of Contents

- [📊 Permission Values](#-permission-values)
- [🔧 Changing Permissions](#-changing-permissions)
- [👤 Changing Ownership](#-changing-ownership)

---

## 📊 Permission Values

**Basic permission values**

```
r: read permission = 4
w: write permission = 2
x: execute permission = 1
```

---

## 🔧 Changing Permissions

### Recursively Change Permissions

**Apply permissions recursively to a folder and its contents**

```bash
  sudo chmod -R 775 /folder_name
```

---

## 👤 Changing Ownership

### Change Owner and Group

**Change the owner and group recursively for a folder**

```bash
  sudo chown -R owner:group /folder_name
```
