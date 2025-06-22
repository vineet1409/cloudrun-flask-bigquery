FROM python:3.10-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv pip sync

COPY app ./app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app.main:app"]
