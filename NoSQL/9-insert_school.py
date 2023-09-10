#!/usr/bin/env python3
"""this module contains a function that insert a new document"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection."""
    return mongo_collection.insert_one(kwargs).inserted_id
