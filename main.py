import requests
from requests.api import head


def read_api_key():
    with open("api_key") as f:
        return f.readline()


api_key = read_api_key()
print("using api key: {}".format(api_key))


def get_auth_header():
    return {'Authorization': 'Bearer {}'.format(api_key)}


def get_base_url():
    return "https://api.sandbox.bigbuy.eu/rest"


def get_catalog_url():
    return "{}/{}".format(get_base_url(), "catalog")


def get_products_url():
    return "{}/{}".format(get_catalog_url(), "products.json")


def get_products_url_with_params(pageSize = 0, page = 0):
    return "{}?pageSize={}&page={}".format(get_products_url(), pageSize, page)


def get_products_request():
    return requests.get(get_products_url_with_params(), headers=get_auth_header())


req1 = get_products_request()
if req1.status_code == 200:
    with open("products.txt", "w") as f:
        f.write(req1.text)
else:
    print(req1.text)
