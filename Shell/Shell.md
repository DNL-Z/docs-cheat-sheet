# SHELL - BASH - ZSH

SHELL
 is a user interface of an operating system, mainly intended to launch other programs and manage their interactions.
ZSH
 is an extended and improved version of
**Bash**
.
The Secure **Shell** (
SSH
) protocol is a method for securely sending commands to a computer over an unsecured network.
SSH uses cryptography to authenticate and encrypt connections between devices.
The
SSH-Agent
 is a helper program that keeps track of users' identity keys and their passphrases

GUI
 => Graphic User Interface

CLI
 => Command Line Interface

## SSH-Folder

```bash
cd .ssh/
```

## SSH-Public Key

```bash
cat .ssh/id-rsa.pub
```

## Add Private Key to macOS - Keychain (SSH-Agent)

```bash
ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

## List Keys from SSH-Agent

```bash
ssh-add -l
```

Oh My **Zsh**
 is an open source, community-driven framework for managing your \*HYPERLINK "https://www.zsh.org/"zsh configuration

## Update Oh My **Zsh**

```bash
omz update
```

## ZPROFILE & ZSHRC

```bash
cat .zprofile
cat .zshrc
```

## HOSTS

```bash
cat /etc/hosts
```

## To know my Public IP

```bash
curl ifconfig.me
```

OR

```bash
ip addr
```
