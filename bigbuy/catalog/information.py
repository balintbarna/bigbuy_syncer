import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_information_url():
    return "{}/{}".format(get_catalog_url(), "productsinformation.json")


def get_information_url_with_params(isoCode = "da"):
    return "{}?isoCode={}".format(get_information_url(), isoCode)


def request_information():
    return requests.get(get_information_url_with_params(), headers=api.get_auth_header())


def get_information():
    r = request_information()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_information():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "information.txt")) as f:
        return json.load(f)


def save_dummy_information():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "information.txt"), "w") as f:
        return json.dump(get_information(), f)


if __name__ == "__main__":
    # save_dummy_information()
    items = get_dummy_information()
    print(items[0:3])
