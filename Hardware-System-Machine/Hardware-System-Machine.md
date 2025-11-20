# 🖥️ Hardware & System Components

Essential hardware components and system protocols for computer architecture.

## 📑 Table of Contents

- [⚙️ Core Processing Components](#-core-processing-components)
  - [CPU - Central Processing Unit](#cpu---central-processing-unit)
  - [GPU - Graphical Processing Unit](#gpu---graphical-processing-unit)
  - [Bus Architecture](#bus-architecture)
- [💾 Memory Systems](#-memory-systems)
  - [RAM - Random Access Memory](#ram---random-access-memory)
  - [ROM - Read Only Memory](#rom---read-only-memory)
- [🌐 Network Protocols](#-network-protocols)
  - [DHCP - Dynamic Host Configuration Protocol](#dhcp---dynamic-host-configuration-protocol)
- [🔧 System Firmware](#-system-firmware)
  - [BIOS - Basic Input Output System](#bios---basic-input-output-system)

---

## ⚙️ Core Processing Components

### CPU - Central Processing Unit

**Central Processing Unit** (measured in MHz - operations/instructions per second)

The processor is an electronic circuit that performs arithmetic and logical operations.

**Key characteristics:**
- Speed measured in MHz (megahertz) or GHz (gigahertz)
- Executes instructions and processes data
- Acts as the brain of the computer

### GPU - Graphical Processing Unit

**Graphical Processing Unit** - A dedicated processor for handling graphics data.

**Purpose:**
- Specialized in rendering graphics and images
- Parallel processing architecture
- Accelerates visual computations

### Bus Architecture

**Data Bus** (MHz & bytes)

The communication pathway between CPU and RAM, transferring data and instructions.

**Flow:**
```
CPU ⟷ Bus (MHz & bytes) ⟷ RAM
```

---

## 💾 Memory Systems

### RAM - Random Access Memory

**Random Access Memory** - Volatile memory (measured in bytes)

RAM is volatile memory that can be infinitely modified when powered by electricity. In computing, RAM temporarily stores files that the computer is currently executing.

**Characteristics:**
- Temporary storage
- Fast read/write access
- Loses data when power is off
- Stores active programs and data

### ROM - Read Only Memory

**Read Only Memory** - Non-volatile memory with read-only content

A type of memory whose content is accessible for reading but not writing. It retains data even when electrical power is absent.

**Characteristics:**
- Permanent storage
- Contains firmware and boot instructions
- Cannot be easily modified
- Retains data without power

---

## 🌐 Network Protocols

### DHCP - Dynamic Host Configuration Protocol

**Dynamic Host Configuration Protocol** - Network protocol for automatic IP configuration

A network/communication protocol responsible for automatically configuring IP addresses on a computer network. It prevents users connecting to a network for the first time from having to manually configure their equipment's IP stack.

**Features:**
- Automatic IP address assignment
- Works with IPv4 and IPv6
- IPv6 can function without DHCP (using SLAAC)
- Simplifies network management

---

## 🔧 System Firmware

### BIOS - Basic Input Output System

**Basic Input Output System** - Fundamental input/output system

A basic program stored on the computer's motherboard that executes before the operating system and collaborates with it.

**Components:**
- **Power-On Self-Test (POST):** Verifies proper functioning of various PC components
- **Bootstrap Loader:** Manages relationships between the processor and machine components
- Initializes hardware before OS boot
- Provides runtime services for operating systems
