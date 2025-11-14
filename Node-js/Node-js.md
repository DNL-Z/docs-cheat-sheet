# ⚙️ Node JS

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.

### Check current Node version

```bash
  node --version
```

### List of available versions

```bash
  nvm ls
```

### Install a new version

```bash
  nvm install v<version>
```

### Change version with NVM

```bash
  nvm use v<version>
```

### Use a specific version by default

```bash
  nvm alias default <version>
```

### Uninstall version

```bash
  nvm uninstall <version>
```

---

### Initialize a new Node project

```bash
  npm init
```

Entry point must be:
server.js

### Installer Nodemon

Nodemon is a tool that helps develop Node.js, based applications by automatically restarting the node application when file changes in the directory are detected.

```bash
  npm install -g nodemon
```

### Installer Express

```bash
  npm install express --save
```

### Mongoose

```bash
  npm install mongoose
```

### Body parser

```bash
  npm install body-parser
```

---

### OpenClassRooms Lesson

Go to the front folder of the lesson
```bash
  cd /basics-node/front-end
```

Run the app
```bash
  npm run start
```

Go to the back folder of the lesson
```bash
 cd /basics-node/back-end
```

Run the server
```bash
  nodemon server
```

OR without nodemon

```bash
  node server
```

---
