#!/usr/bin/python
from functools import reduce 
from product import Product


def main(list_of_products_as_dict): 
    products = convert_into_products(list_of_products_as_dict)
    total_value = calculate_total_value(products)
    discount_percentage = calculate_discount_percentage(products)
    discount_amount = calculate_discount_amount(total_value, discount_percentage)
    final_value = total_value - discount_amount

    products_message = ' '.join(map(lambda p: str(p.to_string()), products))
    discount_message = 'Final value: {}, discount {}%, discount amount: {}'.format(final_value, discount_percentage, discount_amount)
    final_message = products_message + '\n' + discount_message
    return final_message


def convert_into_products(list_of_products_as_dict):
    products = list(map(convert_into_product, list_of_products_as_dict))
    return products


def calculate_total_value(products):
    products_amounts = list(map(lambda p: p.amount, products))
    sum_function = lambda x, y: x + y
    return reduce(sum_function, products_amounts)


def calculate_discount_percentage(products):
    if len(products) == 0:
        return 0

    cheapest_product = get_cheapest_product(products)
    discount = cheapest_product.amount / len(products)
    discount = round(discount, 2)
    return discount


def calculate_discount_amount(total_value, discount):
    final_value = (total_value * discount) / 1
    final_value = round(final_value, 2)
    return final_value


def get_cheapest_product(products):
    return min(products, key=lambda p: p.amount)


def convert_into_product(dict):
    name = dict["name"]
    amount = dict["amount"]
    product = Product(name, amount)
    return product
