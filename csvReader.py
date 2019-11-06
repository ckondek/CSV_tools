#! /usr/bin/env python3

import argparse
import csv
import os.path
import json

from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path",type=str, help="Choose path of CSV File")
args = parser.parse_args()

def searchResult(object):
    searchTerm=input("Enter search Term:--> ")
    return [item for item in object for value in list(item.values()) if searchTerm in value]
def sumList(resultList, **kwargs):
    return sum([Decimal(row['Betrag'].replace(",",".")).quantize(Decimal('.01')) for row in resultList],0)


try:
    try:
        with open(args.path, newline='', encoding='iso-8859-1') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            object=[dict(item) for item in reader]
            print(sumList(searchResult(object)))



    except UnicodeDecodeError as e:
        print(e)
        print("Quitting program")

except FileNotFoundError as e:
    print(e)
    print("Quitting program")
