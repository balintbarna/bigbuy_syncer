import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
from bigbuy.catalog import product as p
from bigbuy.catalog import variation as v


def get_products(dummy = False):
    return p.get_products() if not dummy else p.get_dummy_products()


def get_variations(dummy = False):
    return v.get_variations() if not dummy else v.get_dummy_variations()


def find_matching_product_and_variant():
    prods = get_products(dummy=True)
    vars = get_variations(dummy=True)
    for variant in vars:
        for product in prods:
            if variant["product"] == product["id"]:
                print("found a match")
                print(product)
                print(find_variants_for_product(product, vars))
                return


def compare_product_and_variant_numbers():
    prods = get_products(dummy=True)
    vars = get_variations(dummy=True)
    print("number of products: {}".format(len(prods)))
    print("number of variants: {}".format(len(vars)))
    orphan_variant_ids = []
    unique_product_ids = []
    for variant in vars:
        product_id = variant["product"]
        if product_id not in unique_product_ids:
            unique_product_ids.append(product_id)
        if not find_product_for_variant(variant, prods):
            orphan_variant_ids.append(variant["id"])
    print("number of unique products in variants list: {}".format(len(unique_product_ids)))
    print("number of orphan variants: {}".format(len(orphan_variant_ids)))


def find_product_for_variant(variant, product_list):
    matching_products = [p for p in product_list if variant_belongs_to_product(variant, p)]
    if len(matching_products) > 1:
        raise Exception("Variant matches multiple products, bad data")
    if len(matching_products) < 1:
        raise Exception("Variant has no matching product in database")


def find_variants_for_product(product, variant_list):
    return [v for v in variant_list if variant_belongs_to_product(v, product)]


def variant_belongs_to_product(variant, product):
    return variant["product"] == product["id"]


if __name__ == "__main__":
    find_matching_product_and_variant()
    compare_product_and_variant_numbers()
