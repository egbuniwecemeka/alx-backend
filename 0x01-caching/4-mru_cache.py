#!/usr/bin/python3
"""MRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds an item to cache related to its key using MRU policy """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.stack.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.stack.pop(-1)
            del self.cache_data[mru_key]
            print(f'DISCARD: {mru_key}')

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Get an item from the cache using its key"""
        if key is None or key not in self.cache_data:
            return None

        # Move key to end of list (Marked as MRU)
        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)
        
        return self.cache_data[key]