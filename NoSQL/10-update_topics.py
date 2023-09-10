#!/usr/bin/env python3
"""this module contains a function that updates the topics."""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school."""
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
