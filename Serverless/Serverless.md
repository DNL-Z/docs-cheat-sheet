# ☁️ Serverless

A comprehensive guide for setting up virtual machines, Kubernetes (K3S), and serverless platforms like Apache OpenWhisk.

**Serverless computing** is a cloud computing model where developers can build and run applications without managing servers. The cloud provider automatically handles the infrastructure, scaling, and resource allocation. This allows developers to focus solely on writing code while paying only for the actual compute time used, rather than for idle server capacity.

## 📑 Table of Contents

- [🖥️ Virtual Machines](#-virtual-machines)
  - [Virtualization vs Emulation](#virtualization-vs-emulation)
  - [Create VM with UTM](#create-vm-with-utm)
  - [Initial Setup](#initial-setup)
  - [System Updates](#system-updates)
  - [Network Tools](#network-tools)
- [☸️ Kubernetes](#-kubernetes)
  - [Install K3S](#install-k3s)
  - [Install Kubectl](#install-kubectl)
  - [Configuration](#configuration)
  - [Kubernetes Dashboard](#kubernetes-dashboard)
  - [Service Account Setup](#service-account-setup)
  - [Common Commands](#common-commands)
- [🔥 Apache OpenWhisk](#-apache-openwhisk)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Deployment](#deployment)
  - [Authentication](#authentication)
  - [Actions Management](#actions-management)
  - [Sequences](#sequences)
  - [Troubleshooting](#troubleshooting)

---

## 🖥️ Virtual Machines

**Virtual Machines (VMs)** are software-based emulations of physical computers that run operating systems and applications just like physical machines. They allow you to run multiple isolated operating systems on a single physical machine, providing flexibility for development, testing, and deployment environments. VMs are essential for creating isolated environments, testing different operating systems, and efficiently utilizing hardware resources.

### Virtualization vs Emulation

**Virtualize:** Can run only the native CPU architecture

**Emulate:** Can run other CPU architectures

### Create VM with UTM

Recommended VM specifications:

- **Image:** Ubuntu 22.04
- **RAM:** 8 GB
- **CPU:** 4 cores
- **Storage:** 64 GB

### Initial Setup

**Install required packages:**

- OpenSSH

**User credentials:**

- Login: `your_username`
- Password: `your_password`

### System Updates

**Update package list:**

```bash
  sudo apt update
```

**Upgrade installed packages:**

```bash
  sudo apt upgrade
```

### Network Tools

**Install net-tools:**

```bash
  sudo apt install net-tools
```

**Get VM network information:**

```bash
  ifconfig
```

This will display your VM's IP address (e.g., `192.168.64.x`)

---

## ☸️ Kubernetes

**Kubernetes** is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It groups containers into logical units for easy management and discovery, handling load balancing, rolling updates, and self-healing of applications. Kubernetes is the industry standard for managing microservices architectures and containerized workloads in production environments.

**K3S** is a lightweight, certified Kubernetes distribution designed for resource-constrained environments, IoT devices, and edge computing. It packages Kubernetes into a single binary of less than 100MB, making it perfect for development environments and small-scale deployments.

### Install K3S

**Install K3S on your VM:**

Visit [https://k3s.io/](https://k3s.io/) for installation instructions.

### Install Kubectl

**Install Kubectl on your local machine:**

For macOS: [https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)

### Configuration

**Copy configuration file from VM to a local machine:**

```bash
  cat /etc/rancher/k3s/k3s.yaml
```

Rename the file to `~/.kube/config` on your local machine and update the server address to your VM's IP.

### Kubernetes Dashboard

**Install Kubernetes Dashboard:**

[https://github.com/kubernetes/dashboard](https://github.com/kubernetes/dashboard)

**Start Kubernetes proxy:**

```bash
  kubectl proxy
```

**Access the dashboard:**

Navigate to: [http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login)

### Service Account Setup

**Create a dashboard service account:**

```bash
  kubectl create serviceaccount dashboard-admin-sa
```

**Create cluster role binding:**

```bash
  kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa
```

**Get access token:**

```bash
  kubectl get secrets
```

```bash
  kubectl describe secret <name_of_dashboard>
```

Copy the token for dashboard authentication.

### Common Commands

**Show all pods in all namespaces:**

```bash
  kubectl get pods --all-namespaces
```

---

## 🔥 Apache OpenWhisk

**Apache OpenWhisk** is an open-source serverless platform that executes functions in response to events at any scale. It allows developers to write small pieces of code (called "actions") that run on-demand without worrying about infrastructure management. OpenWhisk supports multiple programming languages and can be triggered by HTTP requests, database changes, message queues, or scheduled events, making it ideal for building event-driven architectures and microservices.

### Prerequisites

**Install Helm:**

```bash
  brew install helm
```

Visit [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/) for other platforms.

### Installation

**Install OpenWhisk CLI:**

```bash
  brew install wsk
```

**OpenWhisk documentation:**

[https://openwhisk.apache.org/](https://openwhisk.apache.org/)

### Deployment

**Deploy OpenWhisk using Helm:**

[https://github.com/apache/openwhisk-deploy-kube#deploy-with-helm](https://github.com/apache/openwhisk-deploy-kube#deploy-with-helm)

```bash
  cd openwhisk-deploy-kube/
```

```bash
  helm install owdev ./helm/openwhisk -n openwhisk --create-namespace -f ./helm/openwhisk/mycluster.yaml
```

### Authentication

**Get authentication key:**

```bash
  grep system helm/openwhisk/values.yaml
```

**Connect to local OpenWhisk:**

```bash
  wsk property set --auth <key_auth>
```

**Connect to remote OpenWhisk:**

```bash
  wsk property set --apihost <apihost_url> --auth <auth_key>
```

**List actions:**

```bash
  wsk -i list
```

### Actions Management

**Create an action:**

```bash
  wsk -i action create <action_name> <file_name_action>
```

**Delete an action:**

```bash
  wsk action delete <action_name>
```

### Sequences

**Create a sequence:**

```bash
  wsk -i action create <sequence_name> --sequence action_name_1,action_name_2,action_name_3
```

**Invoke a sequence:**

```bash
  wsk -i action invoke <sequence_name> --result
```

**Invoke with parameters:**

```bash
  wsk -i action invoke <sequence_name> --result -p <name> <param>
```

### Troubleshooting

**Common error: "The action did not return a dictionary"**

OpenWhisk actions must return a dictionary object. See: [https://stackoverflow.com/questions/48755072/openwhisk-error-the-action-did-not-return-a-dictionary](https://stackoverflow.com/questions/48755072/openwhisk-error-the-action-did-not-return-a-dictionary)

---
