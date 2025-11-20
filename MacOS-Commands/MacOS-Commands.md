# 🍏 macOS Commands

Command-line utilities for customizing and managing macOS system settings, including Dock configuration, Launchpad management, and system preferences.

## 📑 Table of Contents

- [🖥️ Dock Configuration](#-dock-configuration)
  - [Speed Up Dock Auto-Hide Animation](#speed-up-dock-auto-hide-animation)
  - [Reset Dock to Default Settings](#reset-dock-to-default-settings)
- [🚀 Launchpad Management](#-launchpad-management)
  - [Reset Launchpad Layout](#reset-launchpad-layout)

---

## 🖥️ Dock Configuration

### Speed up Dock Auto-Hide Animation

**Configure the Dock to show faster on hover**

```bash
  defaults write com.apple.dock autohide-delay -float 0
  defaults write com.apple.dock autohide-time-modifier -float 0.4
  killall Dock
```

### Reset Dock to Default Settings

**Restore the Dock animation settings to default values**

```bash
  defaults delete com.apple.dock autohide-delay
  defaults delete com.apple.dock autohide-time-modifier
  killall Dock
```

---

## 🚀 Launchpad Management

### Reset Launchpad Layout

**Reset the Launchpad to its default organization**

```bash
  defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock
```
