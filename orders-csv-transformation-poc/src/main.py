#!/usr/bin/python

import os
import csv
import sys
import pandas as pd
from order import Order
from assets import assets_map

max_orders_per_output_file_limit = 90

def get_b3_orders():
    b3_orders = []
    files = get_files_from_resources()
    for file in files:
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            raw_ticker = row['Código de Negociação']
            ticker = assets_map.get(raw_ticker, raw_ticker)
            date = row['Data do Negócio']
            price = row['Preço']
            quantity = row['Quantidade']
            type = row['Tipo de Movimentação']
            b3_order = Order(ticker, date, price, quantity, type)
            b3_orders.append(b3_order)

    print('Total B3 orders:', len(b3_orders))
    return b3_orders


def get_files_from_resources():
    root_dir = "resources"
    filesnames = set()

    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            rel_dir = os.path.relpath(dir_, root_dir)
            rel_file = os.path.join(rel_dir, root_dir, file_name)
            filesnames.add(rel_file)
        
    return filesnames


def divide_chunks(list, chunk_size): 
    for i in range(0, len(list), chunk_size):  
        yield list[i:i + chunk_size] 


def main():
    print('Start process to transform order')
    b3_orders = get_b3_orders()
    orders_chunks = list(divide_chunks(b3_orders, max_orders_per_output_file_limit))

    base_number = 1
    file_base_name = 'ordens{number}.csv'
    headers = ["Código", " Data", " Valor", " Quantidade", " Tipo", " Despesas"]
    for orders_chunk in orders_chunks:
        file_name = file_base_name.format(number = base_number)
        print(file_name)
        base_number += 1
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file, delimiter =',')
            writer.writerow(headers)
            for order in orders_chunk:
                attributes_list = order.attributes_to_list()
                writer.writerow(attributes_list)


if __name__ == '__main__':
    main()
