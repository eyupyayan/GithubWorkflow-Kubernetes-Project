# DevOps Demo Project

Et ende-til-ende lokalt DevOps-prosjekt for læring av:

- Docker
- Kubernetes
- Helm
- ArgoCD
- Prometheus
- Grafana
- GitHub Actions

Prosjektet er laget for å være **beginner-friendly**, men samtidig realistisk nok til å vise hvordan en moderne leveransekjede kan se ut fra kode til deploy og monitoring.

---

## Mål

Målet med prosjektet er å lære hele flyten:

1. Lage og containerisere en Python-app
2. Bygge og pushe image til Docker Hub
3. Deploye appen til lokal Kubernetes med Helm
4. Styre deploy via ArgoCD og GitOps
5. Overvåke appen med Prometheus og Grafana
6. Automatisere bygg/testing med GitHub Actions

---

## Teknologistack

- **Python + Flask** for appen
- **Docker** for containerisering
- **Docker Hub** som image registry
- **Kubernetes (Docker Desktop)** som lokalt cluster
- **Helm** for templating og releases
- **ArgoCD** for GitOps deployment
- **Prometheus** for metrics
- **Grafana** for dashboards
- **GitHub Actions** for CI pipeline

---

## Prosjektstruktur

```text
devops-demo/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── config.py
│   └── storage.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yaml
├── task-service-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── values-dev.yaml
│   ├── values-prod.yaml
│   └── templates/
│       ├── _helpers.tpl
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── configmap.yaml
│       ├── hpa.yaml
│       └── NOTES.txt
└── argocd/
    ├── app-dev.yaml
    └── app-prod.yaml