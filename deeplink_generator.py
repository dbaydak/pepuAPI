import requests

from authorization import get_access_token


campaign_id = 39121

upl = 'https://shopee.co.id/Electronics-cat.11044258'
subid = 'twertawreg'
subid1 = ''
subid2 = ''
subid3 = ''
subid4 = ''


def admitad_deeplink():
    """
    Generates a deeplink using the Admitad Deeplink Generator API.

    Args:
        campaign_id (int): The ID of the Admitad campaign.
        upl (str, optional): The URL of the landing page to link to.
        subid (str, optional): SubID for tracking.
        subid1 (str, optional): SubID1 for tracking.
        subid2 (str, optional): SubID2 for tracking.
        subid3 (str, optional): SubID3 for tracking.
        subid4 (str, optional): SubID4 for tracking.

    Returns:
        dict: The JSON response from the Admitad API containing the generated deeplink.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    Example:
        deeplink_data = admitad_deeplink(campaign_id=12345, upl='https://example.com', subid='my_subid')
        deeplink = deeplink_data.get('deeplink')
        if deeplink:
            print(f"Generated Deeplink: {deeplink}")
    """
    url = f'https://api.admitad.com/deeplink/22162/advcampaign/{campaign_id}/'
    params = {
        'subid': subid,
        'subid1': subid1,
        'subid2': subid2,
        'subid3': subid3,
        'subid4': subid4,
        'ulp': upl
    }
    headers = {
        'Authorization': f'Bearer {get_access_token()}',
        'Content-Type': 'application/json',
        'Cookie': 'path_language=en'
    }
    response = requests.get(url=url, headers=headers, params=params)
    # Raise an exception for bad status codes
    response.raise_for_status()
    return response.json()

print(admitad_deeplink())
