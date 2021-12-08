import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_products_url():
    return "{}/{}".format(get_catalog_url(), "products.json")


def get_products_url_with_params(pageSize = 0, page = 0):
    return "{}?pageSize={}&page={}".format(get_products_url(), pageSize, page)


def request_products():
    return requests.get(get_products_url_with_params(), headers=api.get_auth_header())


def get_products():
    r = request_products()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_products():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "products.txt")) as f:
        return json.load(f)


if __name__ == "__main__":
    dummy_products = get_dummy_products()
    print(dummy_products[1:3])
