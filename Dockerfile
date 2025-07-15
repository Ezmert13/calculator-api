# Stage 1: Build & Test
FROM python:3.11-slim AS builder
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install pytest
RUN pytest

# Stage 2: Production-only
FROM Python:3.11-slim
WORKDIR /app
COPY app.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
