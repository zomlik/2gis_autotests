import requests
from pydantic import ValidationError
from models.get_regions import GetRegions


class ApiClient:
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    def get(self, url: str, query: dict = None):
        self.response = requests.get(url, query, timeout=self._TIMEOUT)
        return self.response

    def post(self, url: str, json_body: dict = None):
        self.response = requests.post(url, json_body, timeout=self._TIMEOUT)
        return self.response

    def put(self, url: str, json_body: dict = None):
        self.response = requests.put(url, json_body, timeout=self._TIMEOUT)
        return self.response

    def patch(self, url: str, json_body: dict = None):
        self.response = requests.patch(url, json_body, timeout=self._TIMEOUT)
        return self.response

    def delete(self, url: str):
        self.response = requests.patch(url, timeout=self._TIMEOUT)
        return self.response

    def head(self, url: str):
        self.response = requests.head(url, timeout=self._TIMEOUT)
        return self.response

    def options(self, url: str):
        self.response = requests.options(url, timeout=self._TIMEOUT)
        return self.response

    def status_code_is(self, expected_code):
        actual_code = self.response.status_code
        assert actual_code == expected_code, f"\nОжидаемый результат: {expected_code} "\
                                             f"\nФактический результат: {actual_code}"

    def get_json(self):
        json_data = self.response.json()
        return json_data

    def json_shema_is_valid(self):
        data = self.get_json()
        try:
            GetRegions(**data)
        except ValidationError:
            raise ValidationError()
