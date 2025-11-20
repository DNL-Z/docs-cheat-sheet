# 🔐 Cybersecurity

## 💥 Brute Force

### 🎯 WPScan

```bash
  # Basic scan
  wpscan --url http://target.com


  # Enumerate users
  wpscan --url http://target.com --enumerate u


  # Brute force attack (for authorized testing only)
  wpscan --url http://target.com --usernames admin --passwords /path/to/wordlist.txt
```

---

## ⚙️ Ansible

Ansible is an open-source automation platform for configuration management, application deployment, and task automation.

### 📦 Installation

```bash
  # Check Ansible version
  ansible --version


  # Install via pip
  pip install ansible


  # Install via package manager (Ubuntu/Debian)
  sudo apt update
  sudo apt install ansible
```

### 💻 Basic Commands

```bash
  # Ping all hosts
  ansible all -m ping


  # Run playbook
  ansible-playbook playbook.yml


  # Check playbook syntax
  ansible-playbook playbook.yml --syntax-check
```

### 📝 Example Playbook

See file: `playbook_test.yml`

---

**⚠️ Note**: All security testing tools and techniques should only be used on systems you own or have explicit written permission to test. Unauthorized access or testing is illegal.
