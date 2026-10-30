
# syntax=docker/dockerfile:1

# Stage 1: Install dependencies
FROM python:3.11.9-slim-bookworm AS builder

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir --upgrade wheel setuptools

# Stage 2: Runtime image
FROM python:3.11.9-slim-bookworm AS runtime

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /opt/venv /opt/venv

# Create a non-root user
RUN useradd --create-home --uid 10001 appuser

# Copy only files needed by the API
COPY src/ ./src/
COPY model.joblib .
COPY churn_v2.csv .

# Run as an unprivileged user
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
