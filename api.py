def read_api_key():
    with open("api_key") as f:
        return f.readline()


api_key = read_api_key()
print("using api key: {}".format(api_key))


def get_auth_header():
    return {'Authorization': 'Bearer {}'.format(api_key)}


def get_base_url():
    return "https://api.sandbox.bigbuy.eu/rest" # TODO change to production URL once it's ready
