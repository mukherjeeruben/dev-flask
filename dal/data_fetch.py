import urllib.request, json
import config


def data_fetch_from_api():
    with urllib.request.urlopen(config.api_url) as url:
        api_raw_data = json.loads(url.read().decode('utf-8'))
        list_data = api_raw_data['data']
        return list_data
