import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_categories_url():
    return "{}/{}".format(get_catalog_url(), "productscategories.json")


def get_categories_url_with_params(isoCode = "da"):
    return "{}?isoCode={}".format(get_categories_url(), isoCode)


def request_categories():
    return requests.get(get_categories_url_with_params(), headers=api.get_auth_header())


def get_categories():
    r = request_categories()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_categories():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "categories.txt")) as f:
        return json.load(f)


def save_dummy_categories():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "categories.txt"), "w") as f:
        return json.dump(get_categories(), f)


if __name__ == "__main__":
    # save_dummy_categories()
    items = get_dummy_categories()
    print(items[0:3])
