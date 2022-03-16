import requests


class BaseService:

    def __init__(self):
        self.url_base = 'http://127.0.0.1:8000/sale/core/'

    def search(self, router):
        response = requests.get(f'{self.url_base}{router}')
        return response.json()
