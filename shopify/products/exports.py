import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import json
import requests
from shopify.products.common import *


def get_products():
    r = request_products()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def request_products():
    return requests.get(get_products_url(), headers=api.get_auth_header())


def get_products_url():
    return "{}.json".format(get_products_base_url())


if __name__ == "__main__":
    products = get_products()["products"]
    print(products)
