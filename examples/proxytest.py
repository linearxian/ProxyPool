import sys
sys.path.append("..")
import requests
from proxypool.setting import TEST_URL

proxy = '95.85.50.218:80'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}

print(TEST_URL)
response = requests.get(TEST_URL, proxies=proxies, verify=False)
if response.status_code == 200:
    print('Successfully')
    print(response.text)