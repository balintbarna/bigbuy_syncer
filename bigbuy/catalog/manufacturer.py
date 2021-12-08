import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_manufacturers_url():
    return "{}/{}".format(get_catalog_url(), "manufacturers.json")


def get_manufacturers_url_with_params(isoCode = "da"):
    return "{}?isoCode={}".format(get_manufacturers_url(), isoCode)


def request_manufacturers():
    return requests.get(get_manufacturers_url_with_params(), headers=api.get_auth_header())


def get_manufacturers():
    r = request_manufacturers()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_manufacturers():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "manufacturers.txt")) as f:
        return json.load(f)


def save_dummy_manufacturers():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "manufacturers.txt"), "w") as f:
        return json.dump(get_manufacturers(), f)


if __name__ == "__main__":
    # save_dummy_manufacturers()
    items = get_dummy_manufacturers()
    print(items[0:3])
