import requests
from dotenv import load_dotenv
import os
def upload_file_to_ipfs(filename):
    """
    Uploads a file to IPFS using the API key and URL from environment variables.
    """
    load_dotenv(dotenv_path='.env')

    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")

    files = {'file': open(f'{filename}', 'rb')}
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.post(api_url, files=files, headers=headers)
    print(response.json())