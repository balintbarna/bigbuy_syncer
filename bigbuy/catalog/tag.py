import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
import json
from bigbuy.catalog.common import *


def get_tags_url():
    return "{}/{}".format(get_catalog_url(), "productstags.json")


def get_tags_url_with_params(isoCode = "da"):
    return "{}?isoCode={}".format(get_tags_url(), isoCode)


def request_tags():
    return requests.get(get_tags_url_with_params(), headers=api.get_auth_header())


def get_tags():
    r = request_tags()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_tags():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "tags.txt")) as f:
        return json.load(f)


def save_dummy_tags():
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "tags.txt"), "w") as f:
        return json.dump(get_tags(), f)


if __name__ == "__main__":
    # save_dummy_tags()
    items = get_dummy_tags()
    print(items[0:3])
