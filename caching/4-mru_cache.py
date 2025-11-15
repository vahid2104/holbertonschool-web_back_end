#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCaching
    Implements Most Recently Used (MRU) caching
    """

    def __init__(self):
        """Initialize MRUCache with order tracking"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in cache_data.
        If cache exceeds MAX_ITEMS, discard the most recently used (MRU) item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update value and mark as MRU
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard MRU item
            mru_key = self.order.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Return value linked to key.
        Return None if key is None or doesn't exist.
        Does not affect MRU order.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
