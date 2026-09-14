# Customer Accounts Microservice

[![CI Build](https://github.com/Nidaa26/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Nidaa26/devops-capstone-project/actions/workflows/ci-build.yaml)

A production-style **Customer Accounts REST API microservice** developed as part of a DevOps capstone project. The application provides CRUD operations for customer accounts and demonstrates software development, automated testing, continuous integration, security, containerization, and Kubernetes deployment.

## Project Overview

The Customer Accounts Microservice is a Flask-based REST API that allows client applications to create, retrieve, update, delete, and list customer accounts.

The project demonstrates key DevOps and software engineering practices including:

* Agile user stories and sprint-based development
* RESTful API design
* Test-driven development and automated testing
* Code quality and linting
* Continuous Integration using GitHub Actions
* API security using Flask-Talisman
* Containerization using Docker
* Kubernetes/OpenShift deployment
* CI/CD automation concepts using Tekton

## Key Features

* Create customer accounts
* Retrieve individual customer accounts
* List all customer accounts
* Update existing customer accounts
* Delete customer accounts
* Health-check endpoint
* RESTful HTTP methods and status codes
* Automated unit and integration tests
* Security headers
* Docker containerization
* Kubernetes deployment configuration
* Automated CI pipeline using GitHub Actions

## REST API Endpoints

| Method | Endpoint         | Description                          |
| ------ | ---------------- | ------------------------------------ |
| GET    | `/`              | Returns service information          |
| GET    | `/health`        | Checks service health                |
| POST   | `/accounts`      | Creates a new customer account       |
| GET    | `/accounts`      | Returns all customer accounts        |
| GET    | `/accounts/<id>` | Returns a specific customer account  |
| PUT    | `/accounts/<id>` | Updates an existing customer account |
| DELETE | `/accounts/<id>` | Deletes a customer account           |

## Technology Stack

### Application

* Python
* Flask
* Flask-SQLAlchemy
* Flask-CORS
* Flask-Talisman
* PostgreSQL

### Testing & Quality

* Nose / nosetests
* Flake8
* Automated test execution
* Test-driven development practices

### DevOps

* GitHub
* GitHub Actions
* Docker
* Kubernetes
* OpenShift
* Tekton

## Project Structure

```text
devops-capstone-project/
│
├── .github/
│   └── workflows/
│       └── ci-build.yaml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── service/
│   └── application source code
│
├── tests/
│   └── automated tests
│
├── tekton/
│   └── CI/CD pipeline configuration
│
├── Dockerfile
├── requirements.txt
├── setup.cfg
├── user-story.md
└── README.md
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Nidaa26/devops-capstone-project.git
cd devops-capstone-project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the automated tests

```bash
nosetests
```

### 4. Run the application

```bash
honcho start
```

The service can then be accessed locally through the configured application port.

## Continuous Integration

The project uses **GitHub Actions** to automatically validate changes pushed to the `main` branch and pull requests targeting `main`.

The CI pipeline performs:

1. Repository checkout
2. Python environment setup
3. Dependency installation
4. Flake8 code-quality checks
5. Automated test execution
6. PostgreSQL service integration

The build status is displayed at the top of this README.

## Docker

The application can be containerized using Docker.

Build the image:

```bash
docker build -t customer-accounts-microservice .
```

Run the container:

```bash
docker run -p 8080:8080 customer-accounts-microservice
```

## Kubernetes

Kubernetes deployment manifests are provided in the `k8s/` directory.

Apply the Kubernetes resources:

```bash
kubectl apply -f k8s/
```

Check the deployment:

```bash
kubectl get deployments
```

Check running pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get services
```

View application logs:

```bash
kubectl logs <pod-name>
```

## Security

Security features implemented in the microservice include:

* HTTP security headers using Flask-Talisman
* Input validation
* Controlled API responses
* Environment-based database configuration
* CORS configuration
* Separation of application configuration from source code

Sensitive credentials and configuration values should not be committed to the repository.

## Agile Development

The project follows an Agile development approach using user stories and incremental sprints.

User stories are documented in:

```text
user-story.md
```

Development is organized around:

* Customer account CRUD functionality
* Automated testing
* Security
* Continuous Integration
* Containerization
* Kubernetes deployment

## CI/CD Workflow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    │
    ├── Run Flake8
    │
    ├── Run Automated Tests
    │
    └── Build Validation
    │
    ▼
Docker
    │
    ▼
Kubernetes / OpenShift
```

## Project Goals

The main goal of this project is to demonstrate how a customer-facing REST API can be developed, tested, secured, containerized, and prepared for cloud-native deployment using modern DevOps practices.

## Author

**Nida Minhaj**

GitHub: [@Nidaa26](https://github.com/Nidaa26)

