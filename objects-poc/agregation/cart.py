from functools import reduce


class Cart:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_product(self):
        for product in self.products:
            print(product.name, product.value)

    def sum_products_values(self):
        product_values = list(map(lambda product: product.value, self.products))
        return reduce((lambda v1, v2: v1 + v2), product_values)
