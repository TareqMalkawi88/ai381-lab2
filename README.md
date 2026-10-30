# \# AI381 Lab 2 – Docker + CI

# 

# \*\*Dr. Tariq Al-Omari\*\* · AI381 Machine Learning Operations · JUST · Fall 2026/27

# 

# \[!\[CI](https://github.com/TareqMalkawi88/ai381-lab2/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TareqMalkawi88/ai381-lab2/actions)

# 

# \## Project Overview

# 

# This project packages a Machine Learning churn prediction model as a FastAPI service using Docker and automates testing, building, security scanning, and publishing through GitHub Actions.

# 

# \## Features

# 

# \- FastAPI prediction API.

# \- Logistic Regression model trained using `churn\_v2.csv`.

# \- Input validation using Pydantic.

# \- Automated tests using Pytest.

# \- Code quality checks using Ruff.

# \- Multi-stage Docker build.

# \- Non-root container execution.

# \- Docker health check.

# \- Automated CI/CD using GitHub Actions.

# \- Container vulnerability scanning using Trivy.

# \- Docker image published to GitHub Container Registry (GHCR).

# 

# \## API Endpoints

# 

# | Method | Endpoint | Description |

# |---|---|---|

# | GET | `/health` | Check API health |

# | POST | `/predict` | Predict customer churn probability |

# 

# \## Run with Docker

# 

# Pull the published image:

# 

# ```bash

# docker pull ghcr.io/tareqmalkawi88/ai381-lab2:86b4065302a0427e7be417e6c8ed9d0681182ec5

# ```

# 

# Run the container:

# 

# ```bash

# docker run -d --name ai381-api -p 8000:8000 ghcr.io/tareqmalkawi88/ai381-lab2:86b4065302a0427e7be417e6c8ed9d0681182ec5

# ```

# 

# Open the API documentation:

# 

# `http://localhost:8000/docs`

# 

# Health check:

# 

# `http://localhost:8000/health`

# 

# \## Run Tests Locally

# 

# ```bash

# pip install -r requirements.txt

# ruff check .

# pytest -v

# ```

# 

# \## Docker Image

# 

# \*\*GHCR Image:\*\*

# 

# `ghcr.io/tareqmalkawi88/ai381-lab2`

# 

# \*\*Image Tag:\*\*

# 

# `86b4065302a0427e7be417e6c8ed9d0681182ec5`

# 

# \*\*Image Digest:\*\*

# 

# `sha256:16a3a84d6821a16a6653ad999965f1703ea70876802888844cab85feea443b25`

# 

# \## CI/CD Pipeline

# 

# GitHub Actions automatically:

# 

# 1\. Runs Ruff and Pytest checks on pull requests.

# 2\. Builds the Docker image on pushes to `main`.

# 3\. Scans the image using Trivy.

# 4\. Publishes the image to GHCR.

# 

# \## Repository

# 

# \[GitHub Repository – AI381 Lab 2](https://github.com/TareqMalkawi88/ai381-lab2)

# 

# \---

# 

# \*\*Course:\*\* AI381 – Machine Learning Operations  

# \*\*University:\*\* Jordan University of Science and Technology (JUST)  

# \*\*Semester:\*\* Fall 2026/27

