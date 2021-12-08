import requests


api_version = "2021-10"


def read_api_key():
    try:
        with open("shopify_api_key") as f:
            return f.readline()
    except:
        raise Exception("Must have top-level file called \"shopify_api_key\" which contains only the api key in one line")


def read_api_pass():
    try:
        with open("shopify_api_password") as f:
            return f.readline()
    except:
        raise Exception("Must have top-level file called \"shopify_api_password\" which contains only the api password in one line")


api_key = read_api_key()
api_pass = read_api_pass()
print("using api key: {}\nand api pass: {}".format(api_key, api_pass))


def get_auth_header():
    return {'X-Shopify-Access-Token': '{}'.format(api_pass)}


def get_base_url():
    return "https://{}.myshopify.com/admin/api/{}".format("markus-dropshipping-test-store", api_version) # TODO change to production URL once it's ready


if __name__ == "__main__":
    url = "{}/shop.json".format(get_base_url())
    print(requests.get(url, headers=get_auth_header()).text)
