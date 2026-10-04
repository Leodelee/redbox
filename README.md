# chatgpt-lab

Isolated AWS MCP to SSM to EC2 coding PoC, now exposed as a FastAPI calculator service.

## Setup

Create a virtual environment and install requirements.txt.

## Run tests

Run: .venv/bin/python -m pytest -q

## Run API

Run: .venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000

Endpoints:
- GET /health
- POST /calculate with JSON such as {"operation": "divide", "a": 8, "b": 2}
