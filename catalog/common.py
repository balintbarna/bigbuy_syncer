import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
from utils import api

def get_catalog_url():
    return "{}/{}".format(api.get_base_url(), "catalog")
