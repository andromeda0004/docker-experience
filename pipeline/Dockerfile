FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

RUN pip install pandas pyarrow

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

WORKDIR /code

ENV PATH="/app/.venv/bin:$PATH"

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py" ]