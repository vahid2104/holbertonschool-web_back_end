#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    Implements a Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """Initialize the MRUCache with an order list"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache
        If the number of items exceeds BaseCaching.MAX_ITEMS,
        discard the most recently used (MRU) item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and mark as most recently used
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item
            mru_key = self.order.pop(-1)
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Return the value linked to key
        Return None if key is None or doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
