from flask import Flask
from google.cloud import bigquery
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    client = bigquery.Client(project=app.config["BQ_PROJECT"])

    @app.route('/')
    def main():
        table_id = app.config["BQ_TABLE_ID"]
        uri = app.config["CSV_GCS_URI"]
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
        )
        load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()
        destination_table = client.get_table(table_id)
        return {"data": destination_table.num_rows}
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
