# 🐚 Shell - Bash - Zsh

A comprehensive reference guide for shell environments, covering Bash, Zsh, SSH, and common shell operations.

## 📑 Table of Contents

- [📖 Overview](#-overview)
  - [Terminology](#terminology)
- [🔐 SSH Operations](#-ssh-operations)
  - [SSH Folder](#ssh-folder)
  - [View Public Key](#view-public-key)
  - [Add Private Key to macOS Keychain](#add-private-key-to-macos-keychain)
  - [List SSH Keys](#list-ssh-keys)
- [⚙️ Zsh Configuration](#-zsh-configuration)
  - [Oh My Zsh](#oh-my-zsh)
  - [Configuration Files](#configuration-files)
- [🌐 Network Operations](#-network-operations)
  - [Check Public IP](#check-public-ip)
  - [Hosts File](#hosts-file)

---

## 📖 Overview

**Shell** is a user interface of an operating system, mainly intended to launch other programs and manage their interactions.

**Zsh** is an extended and improved version of **Bash** with additional features and customization options.

**SSH (Secure Shell)** protocol is a method for securely sending commands to a computer over an unsecured network. SSH uses cryptography to authenticate and encrypt connections between devices.

**SSH-Agent** is a helper program that keeps track of users' identity keys and their passphrases.

### Terminology

- **GUI** - Graphic User Interface
- **CLI** - Command Line Interface

---

## 🔐 SSH Operations

### SSH Folder

Navigate to the SSH configuration directory:

```bash
  cd ~/.ssh/
```

### View Public Key

Display your SSH public key:

```bash
  cat ~/.ssh/id_rsa.pub
```

### Add Private Key to macOS Keychain

Add your private SSH key to the macOS Keychain (SSH-Agent):

```bash
  ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

### List SSH Keys

List all keys currently managed by the SSH-Agent:

```bash
  ssh-add -l
```

---

## ⚙️ Zsh Configuration

### Oh My Zsh

**Oh My Zsh** is an open source, community-driven framework for managing your [Zsh configuration](https://www.zsh.org/).

**Update Oh My Zsh:**

```bash
  omz update
```

### Configuration Files

View your Zsh configuration files:

**View .zprofile:**

```bash
  cat ~/.zprofile
```

**View .zshrc:**

```bash
  cat ~/.zshrc
```

---

## 🌐 Network Operations

### Check Public IP

Retrieve your public IP address:

**Using curl:**

```bash
  curl ifconfig.me
```

**Using ip command:**

```bash
  ip addr
```

### Hosts File

View the hosts file for local DNS resolution:

```bash
  cat /etc/hosts
```
