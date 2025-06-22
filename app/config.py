import os

class Config:
    BQ_PROJECT = os.getenv("BQ_PROJECT", "mlops-project-462702")
    BQ_TABLE_ID = os.getenv("BQ_TABLE_ID", "mlops-project-462702.test_schema.us_states")
    CSV_GCS_URI = os.getenv("CSV_GCS_URI", "gs://vineet-udemy-bucket/cloud-run-demo/us-states.csv")
