import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
import requests
from bigbuy import api

def get_catalog_url():
    return "{}/{}".format(api.get_base_url(), "catalog")


if __name__ == "__main__":
    url = "{}/productvariations/{}.json".format(get_catalog_url(), 14368)
    print(requests.get(url, headers=api.get_auth_header()).text)
