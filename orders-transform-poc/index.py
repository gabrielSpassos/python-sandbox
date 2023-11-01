#!/usr/bin/python

import re
import csv
import sys
from pdfquery import PDFQuery
from order import RawOrder, StockOrder
from assets import assets_map

order_type_map = {'C': 'Compra', 'V': 'Venda'}


def convert_orders_to_csv():
    limit = 90
    orders = get_stock_orders()
    orders_chunks = list(divide_chunks(orders, limit))

    base_number = 1
    file_base_name = 'ordens{number}.csv'
    headers = [" Código", " Data", " Valor", " Quantidade", " Tipo", " Despesas"]
    for orders_chunk in orders_chunks:
        file_name = file_base_name.format(number = base_number)
        print(file_name)
        base_number += 1
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for order in orders_chunk:
                attributes_list = order.attributes_to_list()
                writer.writerow(attributes_list)


def get_stock_orders():
    date = get_date()
    raw_orders = get_raw_orders()
    list_of_orders = []
    for order in raw_orders:
        ticker = assets_map[order.description]
        order_type = order_type_map[order.type]

        stock_order = StockOrder(ticker, date, order.unit_value, order.quantity, order_type)
        list_of_orders.append(stock_order)
    
    return list_of_orders


def get_date():
    pdf = PDFQuery('Nota.pdf')
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]

    date = text[2]

    print('Date: ', date)
    return date.strip()


def get_raw_orders():
    formatted_raw_orders = format_formatted_raw_orders()
    unformatted_raw_orders = format_unformatted_raw_orders()
    orders = formatted_raw_orders + unformatted_raw_orders
    print('Total orders:', len(orders))
    return orders


def format_unformatted_raw_orders():
    with open('nota-mal-formatada.txt', 'r') as file:
        data = file.read()

        if data.strip() == '':
            return []
        
        dataWithRawSeparator = re.sub('(D|C)\n', '###\n', data)
        lines = dataWithRawSeparator.split(sep = "###\n")
        return format_to_raw_orders(lines)


def format_formatted_raw_orders():
    with open('nota-bem-formatada.txt', 'r') as file:
        data = file.read()

        if data.strip() == '':
            return []

        lines = data.split(sep = "\n")
        return format_to_raw_orders(lines)


def format_to_raw_orders(order_lines):
    list_of_orders = []
    for line in order_lines:
            line_without_linebreaker = re.sub('\n', ' ', line)
            market = re.search('(\d-[a-zA-Z]+)', line_without_linebreaker).group().strip()
            order_type = re.search(' (C|V) ', line_without_linebreaker).group().strip()
            market_type = re.search('(FRACIONARIO|VISTA)', line_without_linebreaker).group().strip()
            description = re.search('%s(.*)%s' % (market_type, ' - '), line_without_linebreaker).group(1).strip()
            quantity = re.search('( - \d+)', line_without_linebreaker).group()
            quantity = re.sub('-', '', quantity).strip()
            amounts = re.findall('(\d+,+\d+)', line_without_linebreaker)
            unit_value = amounts[0]
            final_value = amounts[1]
            order = RawOrder(market, order_type, market_type, description, quantity, unit_value, final_value)
            list_of_orders.append(order)
    return list_of_orders


def divide_chunks(list, chunk_size): 
    for i in range(0, len(list), chunk_size):  
        yield list[i:i + chunk_size] 


convert_orders_to_csv()