# **Mac** commands

## **Apple** Dock => faster on hover to show

```bash
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.4
killall Dock
```

## **Apple** Dock => to setup by default

```bash
defaults delete com.apple.dock autohide-delay
defaults delete com.apple.dock autohide-time-modifier
killall Dock
```

## **Apple** Launchpad => reset by default

```bash
defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock
```
