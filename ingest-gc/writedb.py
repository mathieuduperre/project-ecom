#!/usr/bin/env python

# Imports the Google Cloud client library
from google.cloud import datastore
import datetime

def run_quickstart():
    # Instantiates a client
    datastore_client = datastore.Client()
    add_task(datastore_client,u'dummydescription')


def add_task(client, description):
    kind = "product"
    key = "Task3"

    task = datastore.Entity(client.key(kind,key),
        exclude_from_indexes=['description'])

    task.update({
        'created': datetime.datetime.utcnow(),
        'description': description,
        'done': False
    })

    client.put(task)
    print task.key

    return task.key

if __name__ == '__main__':
    run_quickstart()