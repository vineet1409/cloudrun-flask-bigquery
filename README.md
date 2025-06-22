# Cloud Run Flask BigQuery Loader

This repo demonstrates a production-grade MLOps pipeline to deploy a Flask application that loads a CSV from GCS into BigQuery, using Google Cloud Run, uv for dependency management, and GitHub Actions for CI/CD.

## Structure

```
app/                # Application code
tests/              # Unit tests
.github/workflows/  # GitHub Actions workflows
Dockerfile          # Production-ready container build
pyproject.toml      # Python dependencies (for uv)
uv.lock             # Lockfile (for uv)
requirements.txt    # For quick local pip install (generated)
```

## Local Development

1. **Install [uv](https://github.com/astral-sh/uv):**
    ```bash
    pip install uv
    ```
2. **Sync dependencies:**
    ```bash
    uv pip sync uv.lock --system
    ```
3. **Run locally:**
    ```bash
    gunicorn app.main:app
    ```

## Deployment (CI/CD)

- On push to `main`, GitHub Actions builds and deploys the app to Cloud Run.
- Requires `GCP_SA_KEY` secret (service account key) in repository secrets.

## Environment Variables

- `BQ_PROJECT`: BigQuery Project ID
- `BQ_TABLE_ID`: BigQuery Table ID
- `CSV_GCS_URI`: GCS URI of CSV file

## Testing

Add tests to `tests/`. Example in `test_main.py`.

## Production Notes

- Uses `gunicorn` as WSGI server
- Fully managed pipeline with best practices

---
