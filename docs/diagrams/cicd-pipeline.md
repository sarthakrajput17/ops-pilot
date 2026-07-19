## 🚀 CI/CD Pipeline

```mermaid
flowchart LR

A[Developer]

A --> B[Git Push]

B --> C[GitHub Repository]

C --> D[GitHub Actions]

D --> E[Install Dependencies]

E --> F[Run Pytest]

F --> G[Build Docker Image]

G --> H[Push Docker Image]
```