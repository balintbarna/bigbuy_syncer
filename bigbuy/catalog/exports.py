import sys, os
if __package__ is None:
    sys.path.append(os.getcwd())
from bigbuy.catalog.list_data_getter import ListDataGetter


class CatalogData():
    def __init__(self, dummy=False) -> None:
        self.products = ListDataGetter("products", "products.txt", dummy)
        self.variants = ListDataGetter("productsvariations", "variations.txt", dummy)
        self.attributes = ListDataGetter("attributes", "attributes.txt", dummy)
        self.tags = ListDataGetter("productstags", "tags.txt", dummy)
        self.information = ListDataGetter("productsinformation", "information.txt", dummy)
        self.manufacturers = ListDataGetter("manufacturers", "manufacturers.txt", dummy)
        self.images = ListDataGetter("productsimages", "images.txt", dummy)
        self.list_of_lists = [
            self.products,
            self.variants,
            self.attributes,
            self.tags,
            self.information,
            self.manufacturers,
            self.images,
        ]


    def find_matching_product_and_variant(self):
        for product in self.products.get_list():
            variants = self.find_variants_for_product(product)
            if len(variants) > 0:
                print("found matching variants")
                print(product)
                print(variants)
                return


    def cross_examine_product_and_variant_numbers(self):
        print("number of products: {}".format(len(self.products.get_list())))
        print("number of variants: {}".format(len(self.variants.get_list())))
        orphan_variant_ids = []
        unique_product_ids = []
        for variant in self.variants.get_list():
            product_id = variant["product"]
            if product_id not in unique_product_ids:
                unique_product_ids.append(product_id)
            if not self.find_product_for_variant(variant):
                orphan_variant_ids.append(variant["id"])
        print("number of unique products in variants list: {}".format(len(unique_product_ids)))
        print("number of orphan variants: {}".format(len(orphan_variant_ids)))


    def find_product_for_variant(self, variant):
        matching_products = [p for p in self.products.get_list() if variant_belongs_to_product(variant, p)]
        if len(matching_products) > 1:
            raise Exception("Variant matches multiple products, bad data")
        if len(matching_products) < 1:
            raise Exception("Variant has no matching product in database")
        return matching_products


    def find_variants_for_product(self, product):
        return [v for v in self.variants.get_list() if variant_belongs_to_product(v, product)]


    def cross_examine_tags_and_products(self):
        print("number of items: {}".format(len(self.get_item_list())))
        print("number of tags: {}".format(len(self.tags.get_list())))
        for tag in self.tags.get_list():
            self.find_item_for_tag(tag)


    def find_item_for_tag(self, tag):
        matching_items = [item for item in self.get_item_list() if tag_belongs_to_item(tag, item)]
        if len(matching_items) > 1:
            raise Exception("Tag matches multiple items, bad data")
        if len(matching_items) < 1:
            raise Exception("Tag has no matching items in database")
        return matching_items

    def get_item_list(self):
        return self.products.get_list() + self.variants.get_list()


    def find_tags_for_item(self, item):
        return [t["tag"] for t in self.tags.get_list() if tag_belongs_to_item(t, item)]


def variant_belongs_to_product(variant, product):
    return variant["product"] == product["id"]


def tag_belongs_to_item(tag, item):
    return tag["sku"] == item["sku"]



if __name__ == "__main__":
    cd = CatalogData(True)
    # for container in cd.list_of_lists:
    #     container.save_dummy_list()
    cd.find_matching_product_and_variant()
    cd.cross_examine_product_and_variant_numbers()
    cd.cross_examine_tags_and_products()
