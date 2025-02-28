import base64
import requests
import os
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv(dotenv_path='variables/.dev.env')

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
scope = (
    'private_data private_data_phone private_data_email websites statistics '
    'banners public_data advcampaigns banners_for_website coupons '
    'advcampaigns_for_website lost_orders manage_broker_application '
    'broker_application deeplink_generator coupons_for_website opt_codes'
)


def get_base64_authorization():
    # Combine string concatenation and base64 encoding
    data = f"{CLIENT_ID}:{CLIENT_SECRET}".encode('utf-8')
    base64_header_bytes = base64.b64encode(data)
    base64_header = base64_header_bytes.decode('utf-8')
    return base64_header


def get_token():
    url = 'https://api.admitad.com/token/'
    headers = {
        'Authorization': f'Basic {get_base64_authorization()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'scope': scope
    }
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(
            f'API request failed with status code: {response.status_code}, '
            f'response: {response.text}'
        )
    return response.json()


def get_access_token():
    authorization_data = get_token()
    if 'access_token' in authorization_data:
        access_token = authorization_data['access_token']
        # print(authorization_data)
        return access_token
    else:
        print('Access token not found in response.')
        print(authorization_data)  # print the full response for debugging.


# print(get_access_token())
