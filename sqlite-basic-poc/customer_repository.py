import sqlite3


class CustomerRepository:
    def __init__(self):
        self.conn = sqlite3.connect('customers.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS customer (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                taxId  VARCHAR(11) NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                registerDate DATE NOT NULL
            );
            '''
        )
        print('Table successfully created.')

    def list_customers(self):
        self.cursor.execute('SELECT * FROM customer')
        print('Customers: ')
        for line in self.cursor.fetchall():
            print(line)

    def insert_customer(self, name, tax_id, email, phone, register_date):
        self.cursor.execute('''
        INSERT INTO customer (name, taxId, email, phone, registerDate)
        VALUES (?,?,?,?,?)
        ''', (name, tax_id, email, phone, register_date))

        self.conn.commit()
        print('Successfully created customer.')

    def insert_many_customers(self, customers):
        self.cursor.executemany(
            '''
            INSERT INTO customer (name, taxId, email, phone, registerDate)
            VALUES (?, ?, ?, ?, ?)
            ''',
            customers
        )
        self.conn.commit()
        print('Successfully created customers.')

    def update_customer(self, id, name, tax_id, email, phone, register_date):
        self.cursor.execute(
            '''
            UPDATE customer
            SET name = ?, taxId = ?, email = ?, phone = ?, registerDate = ? 
            WHERE id = ?
            ''',
            (name, tax_id, email, phone, register_date, id)
        )
        self.conn.commit()
        print('Successfully updated customer id', id)

    def delete_customer(self, id):
        self.cursor.execute('DELETE FROM customer WHERE id = ?', (id, ))
        self.conn.commit()
        print('Successfully deleted customer id', id)
