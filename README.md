CyberArena Platform Infrastructure

Automated CI/CD pipeline for deploying a microservice platform using Kubernetes (Kind) and GitHub Actions.

CI/CD Pipeline
🏗 Architecture

This project implements a "Shift-Left" infrastructure testing approach. Instead of testing deployments locally, every git push triggers an ephemeral Kubernetes cluster in CI/CD to validate the infrastructure.
⚙️ Tech Stack

    Containerization: Docker
    Orchestration: Kubernetes (Kind for local/CI)
    CI/CD: GitHub Actions
    Container Registry: GitHub Container Registry (GHCR)

🚀 How it works

    Code is pushed to the main branch.
    GitHub Actions builds the app/ into a Docker image.
    The image is tagged with the Git commit SHA and pushed to GHCR.
    An ephemeral kind Kubernetes cluster is created.
    The newly built image is loaded into the kind cluster.
    kubectl apply deploys the Kubernetes manifests.
    An automated healthcheck (curl) validates the deployment.
    The temporary cluster is destroyed.
