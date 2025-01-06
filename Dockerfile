FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app
WORKDIR /app
RUN uv sync --frozen

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9999"]
