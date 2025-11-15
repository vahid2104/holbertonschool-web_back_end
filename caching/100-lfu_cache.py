#!/usr/bin/env python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())
            candidates = [k for k in self.order if self.freq[k] == min_freq]
            discard_key = candidates[0]
            del self.cache_data[discard_key]
            del self.freq[discard_key]
            self.order.remove(discard_key)
            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item
        self.freq[key] = 1
        self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
