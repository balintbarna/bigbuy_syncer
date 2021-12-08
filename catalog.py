import requests
import json
import api


def get_catalog_url():
    return "{}/{}".format(api.get_base_url(), "catalog")


def get_products_url():
    return "{}/{}".format(get_catalog_url(), "products.json")


def get_products_url_with_params(pageSize = 0, page = 0):
    return "{}?pageSize={}&page={}".format(get_products_url(), pageSize, page)


def request_products():
    return requests.get(get_products_url_with_params(), headers=api.get_auth_header())


def get_products():
    req1 = request_products()
    if req1.status_code == 200:
        return json.load(req1.text)
    else:
        print(req1.text)
        return None


def get_dummy_products():
    with open("products.txt") as f:
        return json.load(f)


if __name__ == "__main__":
    print(get_dummy_products()[0])
