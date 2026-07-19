## 📈 Monitoring Architecture

```mermaid
flowchart LR

A[Flask Application]

B[PostgreSQL]

A --> C[Prometheus]

A --> D[Promtail]

D --> E[Loki]

C --> F[Grafana]

E --> F
```