import os
import sys
import requests
# from bs4 import BeautifulSoup
#
# dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, dir)
#
#
# def get_proxy():
#     r = requests.get('http://127.0.0.1:5000/get')
#     proxy = BeautifulSoup(r.text, "lxml").get_text()
#     return proxy
#
#
# def crawl(url, proxy):
#     proxies = {'http': proxy}
#     r = requests.get(url, proxies=proxies)
#     return r.text
#
#
# def main():
#     proxy = get_proxy()
#     html = crawl('http://docs.jinkan.org/docs/flask/', proxy)
#     print(html)

import requests

PROXY_POOL_URL = 'http://localhost:6379/get'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

if __name__ == '__main__':
    get_proxy()

