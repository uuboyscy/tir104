"""
https://cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python
"""
import os

# Import the Secret Manager client library.
from google.cloud import secretmanager
from google.oauth2.service_account import Credentials


SECRET_MANAGER_CREDENTIALS_FILE_PATH = "bigquery-user.json"
CREDENTIALS = Credentials.from_service_account_file(SECRET_MANAGER_CREDENTIALS_FILE_PATH)

client = secretmanager.SecretManagerServiceClient(credentials=CREDENTIALS)

project_id = "notional-zephyr-229707"
secret_id = "tir104-secret"
version_id = 1
name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

response = client.access_secret_version(request={"name": name})

# Print the secret payload.
#
# WARNING: Do not print the secret in a production environment - this
# snippet is showing how to access the secret material.
payload = response.payload.data.decode("UTF-8")
print(payload)