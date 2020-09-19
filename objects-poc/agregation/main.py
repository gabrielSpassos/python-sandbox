from cart import Cart
from product import Product

cart = Cart()

t_shirt = Product('t-shirt', 50)
shoe = Product('shoe', 90)
shorts = Product('shorts', 60)

cart.insert_product(t_shirt)
cart.insert_product(shoe)
cart.insert_product(shorts)

cart.list_product()

print('Total card value: R$', cart.sum_products_values())
