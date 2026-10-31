# AI381 Lab 2 – Docker + CI

**Dr. Tariq Al-Omari** · AI381 Machine Learning Operations · JUST · Fall 2026/27

[![CI](https://github.com/TareqMalkawi88/ai381-lab2/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TareqMalkawi88/ai381-lab2/actions)

## Project Overview

This project packages a Machine Learning churn prediction model as a FastAPI service using Docker and automates testing, building, security scanning, and publishing through GitHub Actions.

## Features

- FastAPI prediction API.
- Logistic Regression model trained using `churn_v2.csv`.
- Input validation using Pydantic.
- Automated tests using Pytest.
- Code quality checks using Ruff.
- Multi-stage Docker build.
- Non-root container execution.
- Docker health check.
- Automated CI/CD using GitHub Actions.
- Container vulnerability scanning using Trivy.
- Docker image published to GitHub Container Registry (GHCR).

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| POST | `/predict` | Predict customer churn probability |

## Run with Docker

Pull the published image:

```bash
docker pull ghcr.io/tareqmalkawi88/ai381-lab2:86b4065302a0427e7be417e6c8ed9d0681182ec5
