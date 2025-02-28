import requests
from datetime import datetime, timedelta

from authorization import get_access_token


def get_admitad_statistics_by_actions():
    url = 'https://api.admitad.com/statistics/actions/'
    parameters = {
        'date_start': (datetime.now() - timedelta(days=5)).strftime('%d.%m.%Y'),
        'date_end': datetime.now().strftime('%d.%m.%Y'),
        'limit': 10,
        'order_by': 'date',
        'offset': '0',
    }
    headers = {
        'Authorization': f'Bearer {get_access_token()}',
        'Content-Type': 'application/json',
        'Cookie': 'path_language=en'
    }
    response = requests.get(url=url, headers=headers, params=parameters)
    return response.json()


print(get_admitad_statistics_by_actions())
