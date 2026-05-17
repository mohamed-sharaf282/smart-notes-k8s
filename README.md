# Smart Notes Kubernetes Platform

A production-style full-stack cloud-native application deployed on Kubernetes.

This project demonstrates real-world Kubernetes concepts including deployments, services, ingress routing, persistent storage, autoscaling, monitoring, secrets management, and health checks.

---

# Project Architecture

Frontend (React)
        ↓
Ingress NGINX
        ↓
Backend API (Flask)
        ↓
PostgreSQL Database

---

# Technologies Used

- Kubernetes
- Docker
- React
- Flask
- PostgreSQL
- NGINX Ingress Controller
- ConfigMaps
- Secrets
- Persistent Volumes
- StatefulSets
- Horizontal Pod Autoscaler (HPA)
- Prometheus
- Grafana
- Helm

---

# Features

- Full Stack Kubernetes Application
- Frontend and Backend Separation
- PostgreSQL Stateful Database
- Persistent Storage using PVC
- ConfigMaps and Secrets Management
- Ingress-Based Domain Routing
- Health Checks (Liveness & Readiness Probes)
- Resource Requests & Limits
- Horizontal Pod Autoscaling
- Monitoring Stack using Prometheus & Grafana
- Internal Service Discovery
- Production-Style Kubernetes Architecture

---

# Project Structure

smart-notes-k8s/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── postgres.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   └── pvc.yaml
│
├── screenshots/
│
├── README.md
│
└── .gitignore

---

# Kubernetes Components

| Component | Purpose |
|---|---|
| Deployment | Manage backend/frontend pods |
| Service | Internal communication |
| Ingress | External routing |
| StatefulSet | PostgreSQL management |
| PVC | Persistent storage |
| ConfigMap | Non-sensitive configs |
| Secret | Sensitive configs |
| HPA | Auto scaling |
| Probes | Health checks |

---

# Monitoring Stack

The project includes monitoring and observability using:

- Prometheus
- Grafana

Metrics monitored:
- CPU Usage
- Memory Usage
- Pod Health
- Cluster Metrics
- Node Metrics

---

# Health Checks

Implemented:
- Liveness Probe
- Readiness Probe

This enables:
- Self-Healing
- Traffic Control
- Better Reliability

---

# Autoscaling

Implemented Horizontal Pod Autoscaler (HPA) based on CPU utilization.

Features:
- Automatic scaling
- Dynamic resource management
- Better performance under load

---

# Screenshots

Add screenshots inside the `screenshots/` folder:

- Frontend UI
- Grafana Dashboard
- Kubernetes Pods
- HPA Scaling
- Ingress Routing

---

# How to Run

## Clone Repository

```bash
git clone YOUR_REPO_URL
cd smart-notes-k8s
 

Start Minikube
Bash
minikube start
Enable Addons
Bash
minikube addons enable ingress
minikube addons enable metrics-server
Deploy Kubernetes Resources
Bash
kubectl apply -f k8s/
Access Application
Frontend:
Plain text
http://app.notes.local
Backend:
Plain text
http://api.notes.local
Author
Mohamed Abdallah Sharaf El-Din
DevOps & Cloud Enthusiast
Faculty of Electronic Engineering
Menofia University
LinkedIn: https://www.linkedin.com/in/mohamed-sharaf-a532b1311?utm_source=share_via&utm_content=profile&utm_medium=member_android
Future Improvements
CI/CD Pipeline using GitHub Actions
AWS EKS Deployment
GitOps using ArgoCD
Advanced Security Policies
Logging Stack Integration