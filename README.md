# 🌐 Proyecto Kubernetes - Despliegue de Aplicaciones Web en Cluster Local

Este proyecto consiste en la creación de un **entorno de Kubernetes en Minikube**, donde se despliegan múltiples aplicaciones web con sus respectivos **Deployments**, **Services** y un **Ingress Controller** para la gestión de rutas de acceso.

---

## 📌 Objetivos
- Montar un cluster local con **Minikube**.
- Implementar aplicaciones web dentro del cluster usando **YAML manifests**.
- Exponer las aplicaciones con **Services (ClusterIP / NodePort / LoadBalancer)**.
- Configurar un **Ingress Controller** para acceder desde el navegador.
- Documentar todo el flujo de despliegue y configuración.

---

## ⚙️ Requisitos Previos
Antes de iniciar, asegúrate de tener instalado en tu máquina:
- [VirtualBox](https://www.virtualbox.org/) o [Docker](https://www.docker.com/) como backend.
- [Minikube](https://minikube.sigs.k8s.io/docs/) (v1.33 o superior).
- [kubectl](https://kubernetes.io/docs/tasks/tools/) para gestionar el cluster.
- (Opcional) [Helm](https://helm.sh/) para instalar el ingress-controller.

---

## 🚀 Pasos de Implementación

### 1️⃣ Iniciar Minikube
```bash
minikube start --driver=virtualbox --memory=4096 --cpus=2