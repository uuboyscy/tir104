"""
Pipeline example:
https://github.com/uuboyscy/ubPython/blob/master/gcp/sample_02_pipeline.ipynb
"""

import os

import pandas as pd
from google.cloud import bigquery
from google.oauth2.service_account import Credentials

# Determine scopes to query data from GoogleSheets
GCP_CREDENTIAL_SCOPE = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/bigquery",
]
credentials = Credentials.from_service_account_file(
    "/Users/uuboy.scy/side-project/tibame/tir104/gcp/notional-zephyr-229707-5375017e41c1.json",
    scopes=GCP_CREDENTIAL_SCOPE
)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Users/uuboy.scy/side-project/tibame/tir104/gcp/notional-zephyr-229707-5375017e41c1.json"

def query_stackoverflow():
    # client = bigquery.Client()
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        client = bigquery.Client(credentials=credentials)
    else:
        client = bigquery.Client()

    query_job = client.query(
        """
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10"""
    )

    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print("{} : {} views".format(row.url, row.view_count))


def query_stackoverflow_to_df() -> pd.DataFrame:
    # client = bigquery.Client()
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        client = bigquery.Client(credentials=credentials)
    else:
        client = bigquery.Client()

    query_job = client.query(
        """
        SELECT
          *
        FROM `notional-zephyr-229707.tir104_demo.gs_demo`
        LIMIT 100"""
    )

    results = query_job.to_dataframe()

    return results



if __name__ == "__main__":
    query_stackoverflow()
    print(query_stackoverflow_to_df())