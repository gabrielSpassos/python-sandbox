class Product:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        self._name = name
    

    @property
    def amount(self):
        return self._amount

    
    @amount.setter
    def amount(self, amount):
        self._amount = amount


    def to_string(self):
        return 'Product: ' + self.name + ' Amount: ' + str(self.amount)
