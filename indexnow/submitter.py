import logging

import requests

from indexnow.errors import ErrorMessages, Exception202, Exception400, Exception403, Exception422, Exception429
from indexnow.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class IndexNow:

    def __init__(self, host: str, key: str, key_location: str = None,
                 search_engine: SearchEngine = SearchEngine.INDEX_NOW):
        self.host = host
        self.key = key
        if key_location:
            self.key_location = key_location
        else:
            self.key_location = '{0}/{1}.txt'.format(self.host, self.key)
        self.search_engine = search_engine

        self.session = requests.Session()

    def set_host(self, host: str):
        self.host = host

    def set_key(self, key: str):
        self.key = key

    def send_url(self, url: str) -> int:
        params = {
            'key': self.key,
            'url': url,
            'keyLocation': self.key_location,
        }
        response = self.session.get(self.search_engine.value, params=params)

        return self.process_response(response)

    def send_urls(self, urls: list) -> int:
        message = {
            'host': self.host,
            'key': self.key,
            'urlList': list(urls),
            'keyLocation': self.key_location,
        }

        response = self.session.post(self.search_engine.value, json=message)

        return self.process_response(response)

    @staticmethod
    def process_response(response):
        if response.status_code == 202:
            raise Exception202(ErrorMessages.ERROR_202)
        if response.status_code == 400:
            raise Exception400(ErrorMessages.ERROR_400)
        if response.status_code == 403:
            raise Exception403(ErrorMessages.ERROR_403)
        if response.status_code == 422:
            raise Exception422(ErrorMessages.ERROR_422)
        if response.status_code == 429:
            raise Exception429(ErrorMessages.ERROR_429)

        return response.status_code
