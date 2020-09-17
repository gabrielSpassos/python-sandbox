#!/usr/bin/python
from person import Person
from product import Product

person = Person('Gabriel', 23)

person.eat('apple')
person.eat('banana')
person.stop_eating()
person.stop_eating()
person.eat('orange')

person.speak('technology')
person.stop_eating()
person.speak('technology')
person.speak('gym')
person.stop_speaking()
person.stop_speaking()
person.speak('financial')
person.get_birthday_year()

print(Person.current_year)

new_person = Person.build_person_by_birthday_year('Jose', 1999)
print(new_person.age)
new_person.get_birthday_year()

Person.create_id()
person.create_id()

t_shirt = Product('T-SHIRT', 50)
t_shirt.discount(10)
print('New price of:', t_shirt.name, t_shirt.price)

shoe = Product('SHOE', 'R$40')
shoe.discount(10)
print('New price of:', shoe.name, shoe.price)
