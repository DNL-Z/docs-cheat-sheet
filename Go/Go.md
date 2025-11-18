# 🦦 GO

Go is an open-source programming language that makes it easy to build simple, reliable, and efficient software.

Go is fast, statically typed, compiled, and has built-in concurrency support.

## 📑 Table of Contents
- [✅ Version Check](#-version-check)
- [⚙️ Environment Setup](#-environment-setup)
- [🧪 Testing and Running](#-testing-and-running)
- [🎨 Code Formatting](#-code-formatting)
- [🐍 Cobra CLI Framework](#-cobra-cli-framework)
- [🗄️ Redis Integration](#-redis-integration)

---

## ✅ Version Check

### Check Go version

```bash
  go version
```

---

## ⚙️ Environment Setup

### Go environment variables (in .zshrc or .bashrc)

```bash
  export GOPATH=$HOME/go
  export GOPROXY=https://proxy.golang.org/
  export PATH="$PATH:$GOPATH/bin"
```

---

## 🧪 Testing and Running

### Run a Go file

```bash
  go run <file_name.go>
```

### Build an executable

```bash
  go build -o <executable_name> main.go
```

### Build the project

```bash
  go build
```

⚠️ **Note**: Always rebuild after making modifications.

### Run tests

```bash
  ./<executable_name> index <directory>
  ./<executable_name> query test
```

---

## 🎨 Code Formatting

### Format Go code

```bash
  go fmt -w <name.go>
```

### Install GoLint

```bash
  go get -u golang.org/x/lint/golint
```

---

## 🐍 Cobra CLI Framework

### Install Cobra

```bash
  go get -u github.com/spf13/cobra/cobra
```

### Initialize a Go module

Create **go.mod** and **go.sum** files:

```bash
  go mod init <module_name>
```

### Initialize a Cobra project

```bash
  cobra init --pkg-name <package_name>
```

### Create go.sum file

```bash
  go mod tidy
```

### Add command files with Cobra (in /cmd)

```bash
  cobra add dump
  cobra add index
  cobra add query
  cobra add search
```

### Manual file additions

Manually add files like **disk.go**, **redis.go**, **results.go**, **text.go** in the **/engine** directory.

---

## 🗄️ Redis Integration

### Install Redis (macOS)

```bash
  brew install redis
```

### Start Redis service

```bash
  brew services start redis
```

### Access Redis CLI

```bash
  redis-cli
```
