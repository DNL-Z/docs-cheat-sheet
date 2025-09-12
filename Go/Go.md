# GO

```bash
go version
```

## **Go** support (dans le fichier .zshrc)

export GOPATH=/Users/vtch_zvtn/Dev/**Go**
export GOPROXY=https://proxy.golang.org/
export PATH="$PATH:$GOPATH/bin"

## **Go** test

```bash
go run « file_name.go »
```

=> Installation de GoLint

```bash
go fmt -w « name.go »
```

$
go get -u golang.org/x/lint/golint

## Cobra

=> Installation de Cobra

```bash
go get -u github.com/spf13/cobra/cobra
```

=> Création de « go.mod » & « go.sum »

```bash
go mod init « name »
```

=> Initialisation de module « search »

```bash
cobra init --pkg-name « name »
```

=> Création de  « go.sum »

```bash
go mod tidy
```

=> Ajouts de fichiers avec cobra, dans /cmd

```bash
cobra add dump
cobra add index
cobra add query
cobra add search
```

=> Ajouts de fichiers :
disk.go, redis.go, results.go, text.go
 à la main dans
/engine

=> Créer un fichier executable « search »

```bash
go build -o « name » main.go
```

=> Toujours rebuild, après les modifs

```bash
go build
```

=> Pour les tests

```bash
./« mon_executable » index <répertoire>
./« mon_executable » query test
```

## Redis

```bash
brew install redis
brew services start redis
redis-cli
```
