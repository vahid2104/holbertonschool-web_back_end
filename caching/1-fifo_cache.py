#!/usr/bin/env python3
"""FIFO caching module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system"""

    def __init__(self):
        """Initialize FIFOCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm"""
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first inserted item
            fifo_key = self.order.pop(0)
            del self.cache_data[fifo_key]
            print(f"DISCARD: {fifo_key}")  # shorter than 79 chars

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
