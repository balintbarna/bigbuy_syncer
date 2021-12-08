import requests


def read_api_key():
    try:
        with open("bigbuy_api_key") as f:
            return f.readline()
    except:
        print("Must have top-level file called \"bigbuy_api_key\" which contains only the secret key in one line")


api_key = read_api_key()
print("using api key: {}".format(api_key))


def get_auth_header():
    return {'Authorization': 'Bearer {}'.format(api_key)}


def get_base_url():
    return "https://api.sandbox.bigbuy.eu/rest" # TODO change to production URL once it's ready


if __name__ == "__main__":
    url = "{}/catalog/productvariations/{}.json".format(get_base_url(), 14368)
    print(requests.get(url, headers=get_auth_header()).text)
