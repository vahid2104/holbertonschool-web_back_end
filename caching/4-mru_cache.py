#!/usr/bin/env python3

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop(-1)
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
