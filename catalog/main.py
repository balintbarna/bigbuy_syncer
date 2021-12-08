import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
from catalog import product as p
from catalog import variation as v


def get_products(dummy = False):
    return p.get_products() if not dummy else p.get_dummy_products()


def get_variations(dummy = False):
    return v.get_variations() if not dummy else v.get_dummy_variations()


if __name__ == "__main__":
    prods = get_products(dummy=True)
    vars = get_variations(dummy=True)
