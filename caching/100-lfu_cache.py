#!/usr/bin/env python3
"""
LFU caching module
Contains LFUCache class which inherits from BaseCaching.
Implements Least Frequently Used (LFU) caching with LRU tie-breaking.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache system that discards the least frequently used items first.
    If multiple items have the same frequency, the least recently used (LRU) is discarded.
    """

    def __init__(self):
        """Initialize LFUCache with frequency and use order tracking."""
        super().__init__()
        self.freq = {}       # Tracks usage frequency of each key
        self.use_order = {}  # Tracks the last use order of each key
        self.counter = 0     # Global counter to track LRU

    def put(self, key, item):
        """Add an item in the cache with LFU + LRU discard logic."""
        if key is None or item is None:
            return

        self.counter += 1

        # If key exists, update value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.use_order[key] = self.counter
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find min frequency
            min_freq = min(self.freq.values())
            # Candidates with the min frequency
            candidates = [k for k, f in self.freq.items() if f == min_freq]
            # If multiple, use LRU based on use_order
            discard_key = min(candidates, key=lambda k: self.use_order[k])
            # Discard the selected key
            del self.cache_data[discard_key]
            del self.freq[discard_key]
            del self.use_order[discard_key]
            print(f"DISCARD: {discard_key}")

        # Add new key
        self.cache_data[key] = item
        self.freq[key] = 1
        self.use_order[key] = self.counter

    def get(self, key):
        """Retrieve an item by key, updating frequency and use_order."""
        if key is None or key not in self.cache_data:
            return None

        self.counter += 1
        self.freq[key] += 1
        self.use_order[key] = self.counter
        return self.cache_data[key]
