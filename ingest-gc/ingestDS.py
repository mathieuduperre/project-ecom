#!/usr/bin/env python

# Imports the Google Cloud client library
from google.cloud import datastore
import datetime
import time
import json
from pprint import pprint

json_file_input = 'bestbuy.json'
NbProduct = 0

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print 'Starting time'
print st

def read_json_input():
    with open(json_file_input) as data_file:
        data = json.load(data_file)
        return data

def write_to_datastore(data):
    # Instantiates a client
    datastore_client = datastore.Client()

    for item in data:
#        for attribute, value in item.items():
         add_product(datastore_client,item)
         NbProduct += 1
    print 'End time'
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print st
    print 'Processed %s products' % NbProduct

def add_product(client, item_to_add):
    kind = "product"

    sku = getSku(item_to_add)
    name = getName(item_to_add)

    task = datastore.Entity(client.key(kind,sku))

    task.update({'created': datetime.datetime.utcnow(),
    'sku':sku,
    'name':name
    })

    client.put(task)
    return

def getSku(tempItem):
    #data = json.loads(jsonData)
    if 'sku' not in tempItem:
        raise ValueError("No SKU for this product")
    for tuple in tempItem.iteritems():
        if 'sku' not in tuple:
            continue
        sku = tuple[1]
        #print("SKU:", sku)

    return sku

def getName(tempItem):
    #data = json.loads(jsonData)
    if 'name' not in tempItem:
        raise ValueError("No NAME for this product")
    for tuple in tempItem.iteritems():
        if 'name' not in tuple:
            continue
        name = tuple[1]
        #print("NAME:", name)

    return name

if __name__ == '__main__':
    write_to_datastore(read_json_input())
