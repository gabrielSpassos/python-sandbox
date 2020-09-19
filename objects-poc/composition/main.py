from customer import Customer

customer1 = Customer('Gabriel', 23)
customer1.insert_address('Porto Alegre', 'RS')
print(customer1.name)
customer1.list_addresses()
print()

customer2 = Customer('Maria', 55)
customer2.insert_address('Rio de Janeiro', 'RJ')
customer2.insert_address('São Paulo', 'SP')
print(customer2.name)
customer2.list_addresses()
print()

customer3 = Customer('João', 70)
customer3.insert_address('Curitiba', 'PR')
print(customer3.name)
customer3.list_addresses()
