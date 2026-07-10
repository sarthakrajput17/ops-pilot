# ops-pilot
# ops-pilot

An end-to-end DevOps platform with CI/CD, Kubernetes, observability, infrastructure automation, and an AI operations copilot for deployment workflows.

## Project Goal
Build a cloud-native DevOps platform around a Flask microservice and PostgreSQL database, then evolve it into an AI-assisted operations system that can help with deployment, monitoring, debugging, and infrastructure workflows.

## Day 1 Scope
- Set up project repository structure
- Build Flask application skeleton
- Connect Flask to PostgreSQL
- Create `/health` endpoint
- Prepare for Dockerization and Kubernetes deployment in later phases

## Initial Project Structure
```bash
ops-pilot/
├── app/
│   ├── src/
│   ├── tests/
│   └── requirements.txt
├── database/
├── docs/
├── .env.example
└── README.md