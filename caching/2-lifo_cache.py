#!/usr/bin/env python3

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.last_key = key
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                print("DISCARD: {}".format(self.last_key))
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key)
