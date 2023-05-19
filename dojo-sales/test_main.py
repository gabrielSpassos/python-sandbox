import unittest

from main import *
from product import Product

class Test(unittest.TestCase):
    dict = {'name': 'product1', 'amount': 1}
    array = [{'name': 'p1', 'amount': 1}, {'name': 'p2', 'amount': 2}, {'name': 'p3', 'amount': 3}]
    products = [Product('p1', 1), Product('p2', 2), Product('p3', 3)]
    message = 'Product: p1 Amount: 1 Product: p2 Amount: 2 Product: p3 Amount: 3\nFinal value: 4.02, discount 0.33%, discount amount: 1.98'
    

    def test_convert_into_product(self):
        product = convert_into_product(self.dict)
        assert "product1" == product.name
        assert 1 == product.amount

    
    def test_convert_into_products(self):
        products = convert_into_products(self.array)
        assert 3 == len(products)

    
    def test_get_cheapest_product(self):
        cheapest_product = get_cheapest_product(self.products)
        assert "p1" == cheapest_product.name
        assert 1 == cheapest_product.amount

    
    def test_calculate_discount_percentage(self):
        discount = calculate_discount_percentage(self.products)
        assert 0.33 == discount

    
    def test_calculate_discount_percentage_with_empty_list(self):
        discount = calculate_discount_percentage([])
        assert 0 == discount


    def test_calculate_total_value(self):
        total_value = calculate_total_value(self.products)
        assert 6 == total_value

    
    def test_calculate_value_with_discount(self):
        final_value = calculate_discount_amount(100, 0.5)
        assert 50 == final_value

    
    def test_main(self):
        result = main(self.array)
        assert self.message == result