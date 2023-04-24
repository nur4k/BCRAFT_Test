FROM python:3.11-slim as builder

WORKDIR /app
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH=$PATH:/etc/poetry/bin

COPY ./pyproject.toml ./poetry.lock ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main

FROM python:3.11-slim
ENV PATH=/app/.venv/bin:$PATH \
    PYTHONPATH=$PYTHONPATH:/app/src
WORKDIR /app
COPY alembic alembic
COPY alembic.ini .
COPY src src
COPY tests tests
COPY main.py ./
RUN mkdir media
COPY --from=builder /app/.venv .venv

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]