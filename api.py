def read_api_key():
    try:
        with open("api_key") as f:
            return f.readline()
    except:
        print("Must have top-level file called \"api_key\" which contains only the secret key in one line")


api_key = read_api_key()
print("using api key: {}".format(api_key))


def get_auth_header():
    return {'Authorization': 'Bearer {}'.format(api_key)}


def get_base_url():
    return "https://api.sandbox.bigbuy.eu/rest" # TODO change to production URL once it's ready
