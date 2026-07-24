# 🚀 Enterprise-Grade DevSecOps & GitOps Pipeline

An automated, end-to-end continuous integration and deployment ecosystem built with **GitHub Actions, SonarQube, Trivy, Docker, ArgoCD, Kubernetes, Prometheus, and Grafana**.

---

## 🏗 System Architecture

This project follows a **GitOps paradigm**, strictly decoupling application source code from declarative infrastructure/deployment manifests across two dedicated repositories:

```text
[ Code Commit ] ➔ [ GitHub Actions ] ➔ [ SonarQube & Trivy Scan ] ➔ [ Docker Hub ]
                                                                             │
[ Grafana Dashboard ] ⇇ [ Prometheus ] ⇇ [ Kubernetes Cluster ] ⇇ [ ArgoCD ]

```

* **Application Repository:** `flazel/Learn_ci-cd` *(Source code, tests, CI pipeline)*
* **GitOps Repository:** `flazel/learn_ci-cd-gitops` *(Kubernetes deployment manifests, resource limits)*

---

## 🛠 Tech Stack & Tools

* **Application Stack:** Python (Flask), Pytest
* **CI / Automation:** GitHub Actions
* **DevSecOps & SAST:** SonarQube, Trivy Image Scanner, Gitleaks, `pip-audit`
* **Artifact Registry:** Docker Hub
* **CD & GitOps Engine:** ArgoCD
* **Orchestration:** Kubernetes (Minikube)
* **Observability & Monitoring:** Kube-Prometheus-Stack (Prometheus & Grafana)

---

## 📊 Proof of Work & Pipeline Stages

### 1. Continuous Integration & DevSecOps

Automated multi-stage workflow executing unit tests, code coverage calculation, static code analysis via SonarQube, secret scanning, dependency vulnerability audits, and Trivy container image scanning upon every `push` to `main`.

### 2. Code Quality & Security Gate

SonarQube Static Application Security Testing (SAST) enforcing code quality, evaluating coverage metrics (achieved **81.8%**), and detecting security hotspots.

### 3. GitOps Continuous Deployment

ArgoCD continuously monitors the GitOps repository for state drifts. Upon new commits (updated Docker image tags), ArgoCD automatically triggers a zero-downtime rolling update on the Kubernetes cluster.

### 4. Full-Stack Cluster Observability

Real-time infrastructure performance, pod-level resource limits/usage, and application health metrics collected by Prometheus exporters and visualized through Grafana dashboards.

---

## 💻 Local Setup & Development

### Prerequisites

* Docker & Minikube installed
* Helm v3+
* Python 3.9+



## 📄 License

Distributed under the **MIT License**.
