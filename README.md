# Ops-Pilot

An end-to-end DevOps platform built using Flask and PostgreSQL. The project will gradually evolve into a cloud-native DevOps platform featuring Docker, Kubernetes, CI/CD, Infrastructure as Code, Monitoring, Logging, and an AI Operations Copilot.

---

# Project Goal

Build a production-style backend while learning real DevOps practices from scratch.

The project starts with a Flask REST API and PostgreSQL database, then expands to include:

- Docker
- Kubernetes
- GitHub Actions CI/CD
- Terraform
- AWS Deployment
- Monitoring (Prometheus & Grafana)
- Logging
- AI-assisted DevOps operations

---

# Tech Stack

- Python 3.12
- Flask
- PostgreSQL
- Docker
- Git
- GitHub
- psycopg2

---

# Project Structure

```text
ops-pilot/
│
├── app/
│   ├── src/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── db.py
│   │   └── config.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── database/
│   └── init.sql
│
├── docs/
│
├── .env
├── .env.example
├── .gitignore
└── README.md
```

---

# Features Completed

## Day 1

- Project setup
- Flask application
- PostgreSQL connection
- Health Check API

---

## Day 2

- Create User API (POST)

---

## Day 3

- Get All Users API
- Get User By ID API

---

## Day 4

- Update User API

---

## Day 5

- Delete User API

---

# REST APIs

## Health Check

```
GET /health
```

Response

```json
{
  "status": "ok",
  "database": "connected"
}
```

---

## Create User

```
POST /users
```

Request

```json
{
  "name":"Sparsh",
  "email":"sparsh@test.com"
}
```

---

## Get All Users

```
GET /users
```

---

## Get User By ID

```
GET /users/{id}
```

---

## Update User

```
PUT /users/{id}
```

Request

```json
{
  "name":"Updated Name",
  "email":"updated@test.com"
}
```

---

## Delete User

```
DELETE /users/{id}
```

---

# Database

Current table:

```
users
```

Columns

- id
- name
- email
- created_at

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/sarthakrajput17/ops-pilot.git
```

---

## Install Dependencies

```bash
pip install -r app/requirements.txt
```

---

## Start PostgreSQL Container

```bash
docker start ops-pilot-postgres
```

---

## Run Flask

```bash
cd app/src

python main.py
```

---

## Current Progress

- Flask Backend
- PostgreSQL Integration
- Full CRUD APIs
- Input Validation
- Duplicate Email Handling
- Dockerized PostgreSQL
- Git Version Control

---

# Upcoming

- Exception Handling
- Unit Testing
- Dockerize Flask
- Docker Compose
- CI/CD Pipeline
- Kubernetes Deployment
- Monitoring
- AI Ops Copilot
