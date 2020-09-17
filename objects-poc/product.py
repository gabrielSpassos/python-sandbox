class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    #Getter
    @property
    def price(self):
        return self._price

    #Setter
    @price.setter
    def price(self, price):
        if isinstance(price, str):
            price = float(price.replace('R$', ''))

        self._price = price
