import urllib.request, json


def data_fetch_from_api(external_url):
    with urllib.request.urlopen(external_url) as url:
        api_raw_data = json.loads(url.read().decode('utf-8'))
        list_data = api_raw_data['data']
        return list_data
