import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


class ListDataGetter():
    def __init__(self, url_part, file_name) -> None:
        self.url_part = url_part
        self.file_name = file_name
        self._list = None


    def get_url(self):
        return "{}/{}.json".format(get_catalog_url(), self.url_part)


    def get_url_with_params(self, pageSize = 0, page = 0, isoCode = "da"):
        return "{}?pageSize={}&page={}&isoCode={}".format(self.get_url(), pageSize, page, isoCode)


    def request_data(self):
        return requests.get(self.get_url_with_params(), headers=api.get_auth_header())


    def get_list(self, dummy=False):
        if not self._list:
            self._list = self.download_list() if not dummy else self.get_dummy_list()
        return self._list


    def download_list(self):
        r = self.request_data()
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            print(r.text)
            return None


    def get_dummy_list(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, self.file_name)) as f:
            return json.load(f)


    def save_dummy_list(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, self.file_name), "w") as f:
            return json.dump(self.get_list(), f)


if __name__ == "__main__":
    category_loader = ListDataGetter("productscategories", "categories.txt")
    category_loader.save_dummy_list()
    items = category_loader.get_dummy_list()
    print(items[0:3])
