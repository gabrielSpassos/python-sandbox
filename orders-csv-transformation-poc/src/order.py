#!/usr/bin/python

class Order:
    def __init__(self, ticker, date, price, quantity, type, cost=0):
            self.ticker = ticker
            self.date = date
            self.price = price
            self.quantity = quantity
            self.type = type
            self.cost = cost

    
    def attributes_to_list(self):
        formatted_price = str(self.price).replace('.', ',')
        list = []
        list.append(str(self.ticker))
        list.append(str(self.date))
        list.append(formatted_price)
        list.append(str(self.quantity))
        list.append(str(self.type))
        list.append(str(self.cost))
        return list

    
    def to_string(self):
        return (str(self.ticker) + ';' 
        + str(self.date) + ';'
        + str(self.price) + ';'
        + str(self.quantity) + ';'
        + str(self.type) + ';'
        + str(self.cost) + ';')
