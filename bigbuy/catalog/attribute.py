import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_attributes_url():
    return "{}/{}".format(get_catalog_url(), "attributes.json")


def get_attributes_url_with_params(isoCode = "da"):
    return "{}?isoCode={}".format(get_attributes_url(), isoCode)


def request_attributes():
    return requests.get(get_attributes_url_with_params(), headers=api.get_auth_header())


def get_attributes():
    r = request_attributes()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_attributes():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "attributes.txt")) as f:
        return json.load(f)


def save_dummy_attributes():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "attributes.txt"), "w") as f:
        return json.dump(get_attributes(), f)


if __name__ == "__main__":
    # save_dummy_attributes()
    dummy = get_dummy_attributes()
    print(dummy[0:3])
