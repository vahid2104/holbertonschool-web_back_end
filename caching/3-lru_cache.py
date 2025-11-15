#!/usr/bin/env python3
"""LRU caching module.
This module defines the LRUCache class that implements
a Least Recently Used (LRU) caching system.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching
    Implements a caching system using Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item: The value to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move key to end to mark it as recently used
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            discarded_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists, else None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move key to end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
