#!/usr/bin/python

class RawOrder:

    def __init__(self, market, type, market_type, description, quantity, unit_value, final_value):
        self.market = market
        self.type = type
        self.market_type = market_type
        self.description = description
        self.quantity = quantity
        self.unit_value = unit_value
        self.final_value = final_value
    
    def to_string(self):
        return ('market: ' + self.market 
        + ' type: ' + self.type 
        + ' market_type: ' + self.market_type 
        + ' description: ' + self.description 
        + ' quantity: ' + self.quantity 
        + ' unit_value: ' + self.unit_value 
        + ' final_value: ' + self.final_value) 

class StockOrder:
    def __init__(self, ticker, date, price, quantity, type, cost=0):
            self.ticker = ticker
            self.date = date
            self.price = price
            self.quantity = quantity
            self.type = type
            self.cost = cost

    
    def attributes_to_list(self):
        list = []
        list.append(str(self.ticker))
        list.append(str(self.date))
        list.append(str(self.price))
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
