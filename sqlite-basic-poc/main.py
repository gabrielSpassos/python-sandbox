from customer_repository import CustomerRepository

customer_repository = CustomerRepository()

customer_repository.create_table()

customer_repository.list_customers()

customer_repository.insert_customer('Jose', '36898050907', 'jose@yahoo.com', '5585989294642', '2020-09-12')

customers = [
    ('Gabriel', '04786356050', 'gabriel@gmail.com', '5569982522833', '2020-09-20'),
    ('Fernanda', '65733181885', 'fernanda@hotmail.com', '5583992571645', '2020-09-20')
]
customer_repository.insert_many_customers(customers)

customer_repository.list_customers()

customer_repository.update_customer(2, 'Gabriel', '04786356050', 'gabriel@gmail.com', '5569982522932', '2020-09-21')

customer_repository.list_customers()

customer_repository.delete_customer(1)
customer_repository.delete_customer(2)
customer_repository.delete_customer(3)

customer_repository.list_customers()

customer_repository.close()
