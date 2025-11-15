#!/usr/bin/env python3
"""
This module defines a LIFO (Last In First Out) caching system.
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFO caching system that inherits from BaseCaching.
    Implements put and get methods following LIFO eviction policy.
    """

    def __init__(self):
        """Initialize the LIFOCache instance and order tracking."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO eviction policy.

        If key or item is None, does nothing.
        If cache exceeds MAX_ITEMS, discards the last added item.
        """
        if key is None or item is None:
            return

        # If key already exists, just update the value
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        # If cache is full, remove the last added item (LIFO)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-1)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        # Add new item and track order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item by key.

        Returns None if key is None or key does not exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
