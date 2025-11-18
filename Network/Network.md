# 🕸️ Network Administration

Network configuration, routing, and virtual machine management for Linux systems, including SSH setup, IP configuration, and routing tables.

## 📑 Table of Contents

- [📦 Package Management](#-package-management)
  - [Update & Upgrade Packages](#update--upgrade-packages)
  - [Install Network Tools](#install-network-tools)
- [🖥️ Virtual Machine Configuration](#-virtual-machine-configuration)
  - [VM Information](#vm-information)
  - [IP Address Information](#ip-address-information)
- [🔐 SSH Configuration](#-ssh-configuration)
  - [Setup SSH Access](#setup-ssh-access)
  - [Connect with SSH Key](#connect-with-ssh-key)
  - [Switch to Root User](#switch-to-root-user)
- [🔧 Network Interface Management](#-network-interface-management)
  - [Configure Network Interfaces](#configure-network-interfaces)
  - [Enable Network Interfaces](#enable-network-interfaces)
- [🛣️ Routing Configuration](#-routing-configuration)
  - [List Existing Routes](#list-existing-routes)
  - [Add Routes](#add-routes)
  - [Delete Routes](#delete-routes)

---

## 📦 Package Management

### Update & Upgrade Packages

**Update package list and upgrade installed packages**

```bash
  sudo apt update
  sudo apt upgrade
```

### Install Network Tools

**Install net-tools package for network configuration utilities**

```bash
  sudo apt install net-tools
```

---

## 🖥️ Virtual Machine Configuration

### VM Information

**Display network interface configuration**

```bash
  ifconfig
```

### IP Address Information

**Calculate IP address details and network information**

```bash
  ipcalc <ip_address>
```

---

## 🔐 SSH Configuration

### Setup SSH Access

**Configure SSH key-based authentication**

To enable SSH access to a VM, create an `authorized_keys` file in the `.ssh` directory on the VM and add your machine's public key `id_rsa.pub`.

> **Note:** Change network access mode from NAT to Bridge for direct network access.

### Connect with SSH Key

**First SSH connection using a public key**

```bash
  ssh -i id_rsa.pub user@<ip_address>
```

### Switch to Root User

**Switch from regular user to root**

```bash
  su -
```

---

## 🔧 Network Interface Management

### Configure Network Interfaces

**Edit the network interfaces configuration file**

Modify `/etc/network/interfaces` to add all network configurations.

### Enable Network Interfaces

**Bring up network interfaces**

```bash
  ifup enp0s8
  ifup enp0s3
```

---

## 🛣️ Routing Configuration

### List Existing Routes

**Display the routing table**

```bash
  route -n
```

### Add Routes

**Add a route from VM (A) to VM (C) via VM (B)**

```bash
  route add -net 10.0.4.0/24 gw 10.0.3.5
```

**Add a return route from VM (C) to VM (A) (to create a round-trip)**

```bash
  route add -net 10.0.3.0/24 gw 10.0.4.4
```

### Delete Routes

**Remove a specific route**

```bash
  route del -net 10.0.4.0/24 gw 10.0.3.5
```
