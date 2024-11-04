import json
from google.oauth2 import service_account

def initialize_credentials(json_file_path):
    with open(json_file_path) as f:
        json_token = json.load(f)
    return service_account.Credentials.from_service_account_info(json_token)
