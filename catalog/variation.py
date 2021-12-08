import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from common import *


def get_variations_url():
    return "{}/{}".format(get_catalog_url(), "productsvariations.json")


def get_variations_url_with_params(pageSize = 0, page = 0):
    return "{}?pageSize={}&page={}".format(get_variations_url(), pageSize, page)


def request_variations():
    return requests.get(get_variations_url_with_params(), headers=api.get_auth_header())


def get_variations():
    r = request_variations()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_variations():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "variations.txt")) as f:
        return json.load(f)


def get_variations_of_product_url(id):
    return "{}/{}/{}.{}".format(get_catalog_url(), "productvariations", id, "json")


def request_variations_of_product(id):
    return requests.get(get_variations_of_product_url(id), headers=api.get_auth_header())


if __name__ == "__main__":
    dummy_vars = get_dummy_variations()
    print(dummy_vars[1:3])
