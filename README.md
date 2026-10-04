# DevOps Lab - CI/CD with GitHub Actions

Flask app with two GitHub Actions pipelines, built for DevOps Lab Task 1.

- **Phase 1 (no AI):** .github/workflows/ci-basic.yml - hand-written: install, test, docker build.
- **Phase 2 (AI-optimized):** .github/workflows/ci-cd.yml - lint (flake8), security scan (bandit), matrix tests (py3.10-3.12), 80% coverage gate, pip and Docker caching, image push to GHCR, staging deploy with smoke test.

## Run locally

    pip install -r requirements-dev.txt
    python -m pytest --cov=app
    flake8 app tests
    docker build -t flask-devops-lab . && docker run -p 5000:5000 flask-devops-lab

See the Actions tab for pipeline runs.
