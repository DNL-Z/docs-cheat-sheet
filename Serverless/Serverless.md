# SERVERLESS

## VM

Virtualize
 = Can run only the
native CPU architecture

Emulate
 = Can run
other CPU architecture

## Create VM with UTM

	- Image: Ubuntu 22.04
	- RAM: 8 GB
	- CPU: 4 cores
	- Memory: 64 GB

## Install

	- OpenSSH

User /
Login : dnl
Password : J…99%

Root /
Login :
Password :

## Update packages

```bash
sudo apt update
```

## Upgrade Packages

```bash
sudo apt upgrade
```

## Install Net-Tools

```bash
sudo apt install net-tools
```

## Informations of VM

```bash
ifconfig
```

=> 192.168.64.8

## KUBERNETES

## Install K3S on my VM

\*HYPERLINK "https://k3s.io/"https://k3s.io/

## Install Kubectl on my machine

\*HYPERLINK "https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/"https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/

## Copy file

k3s.yaml
 from my VM to my machine

```bash
cat /etc/rancher/k3s/k3s.yaml
```

=> rename to :
.kube/config
 (on my machine)

## Install Kubernetes Dashboard

\*HYPERLINK "https://github.com/kubernetes/dashboard"https://github.com/kubernetes/dashboard

## Start Kubernetes

```bash
kubectl proxy
```

## URL to access on Kubernetes Dashboard

\*HYPERLINK "http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login"http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

 Get Token

## Create the dashboard service account

```bash
kubectl create serviceaccount dashboard-admin-sa
```

```bash
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa
```

```bash
kubectl get secrets
```

```bash
kubectl describe secret <name_of_dashboard>
```

=> copy token for access

## Show all namespaces

```bash
kubectl get pods --all-namespaces
```

## Install

Helm
 on my machine

\*HYPERLINK "https://helm.sh/fr/docs/intro/install/"https://helm.sh/fr/docs/intro/install

```bash
brew install helm
```

## Install

OpenWhisk
 on my machine

```bash
brew install wsk
```

## Informations of OpenWhisk

\*HYPERLINK "https://openwhisk.apache.org/"https://openwhisk.apache.org/

## Deploy OpenWhisk from **Git**

\*HYPERLINK "https://github.com/apache/openwhisk-deploy-kube#deploy-with-helm"https://github.com/apache/openwhisk-deploy-kube#deploy-with-helm

```bash
cd openwhisk-deploy-kube/
```

```bash
helm install owdev ./helm/openwhisk -n openwhisk --create-namespace -f ./helm/openwhisk/mycluster.yaml
```

## Get Key authentification

```bash
grep system helm/openwhisk/values.yaml
```

## Connect to local OpenWhisk

```bash
wsk property set --auth <key_auth>
```

## Connect to Zino’s OpenWhisk

```bash
wsk property set --apihost  https://ow.services.eemi.tech --auth 61901a52-cc60-4e70-9c0e-31ffac6216c9:IMrwqAF80kUR4CVxbo80Q82bPYCqvMvYDLu4HdUGyBXymPj1Nw78Y94PCCZioaxB
```

## List

```bash
wsk -i list
```

## Create action

```bash
wsk -i action create <action_name> <file_name_action>
```

## Delete action

```bash
wsk action delete <action_name>
```

## Create sequence

```bash
wsk -i action create <sequence_name> --sequence action_name_1,action_name_2,action_name_3…
```

## Invoke

```bash
wsk -i action invoke <sequence_name> --result (-r)
```

```bash
wsk -i action invoke <sequence_name> --result -p <name> <param>
```

---

Error with 1st action OpenWhisk :

\*HYPERLINK "https://stackoverflow.com/questions/48755072/openwhisk-error-the-action-did-not-return-a-dictionary"https://stackoverflow.com/questions/48755072/openwhisk-error-the-action-did-not-return-a-dictionary

---
