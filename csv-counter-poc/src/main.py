#!/usr/bin/python
import csv


def convert_to_string_list(value):
    return value.replace("[", "").replace("]", "").replace("\"", "").replace(" ", "")


with open('liability2.csv', mode ='r') as file:
    accountIds = []
    reader = csv.reader(file)
    next(reader, None)  # skip the headers
    for line in reader:
        result = list(map(convert_to_string_list, line))
        accountIds.extend(result)
    
    print(accountIds)
    not_duplicated_accountIds = set(accountIds)

    print("Total accountIds found:", len(accountIds))
    print("Total not duplicated accountIds:", len(not_duplicated_accountIds))