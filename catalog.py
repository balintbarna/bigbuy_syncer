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


def get_variations_url():
    return "{}/{}".format(get_catalog_url(), "productsvariations.json")


def get_variations_url_with_params(pageSize = 0, page = 0):
    return "{}?pageSize={}&page={}".format(get_variations_url(), pageSize, page)


def request_variations():
    return requests.get(get_variations_url_with_params(), headers=api.get_auth_header())


def get_variations_of_product_url(id):
    return "{}/{}/{}.{}".format(get_catalog_url(), "productvariations", id, "json")


def request_variations_of_product(id):
    return requests.get(get_variations_of_product_url(id), headers=api.get_auth_header())


def get_products():
    r = request_products()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


def get_dummy_products():
    with open("products.txt") as f:
        return json.load(f)


def get_variations():
    r = request_variations()
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print(r.text)
        return None


if __name__ == "__main__":
    dummy_products = get_dummy_products()
    print(dummy_products[1])
    all_vars = get_variations()
    with open("variations.txt", "w") as f:
        json.dump(all_vars,f)

