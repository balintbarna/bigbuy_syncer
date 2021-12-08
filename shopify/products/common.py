import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
from shopify import api


def get_products_base_url():
    return "{}/{}".format(api.get_base_url(), "products")


if __name__ == "__main__":
    url = "{}.json".format(get_products_url())
    print(requests.get(url, headers=api.get_auth_header()).text)
