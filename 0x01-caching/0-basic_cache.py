#!/usr/biin/env python3
""" Creates a cache class that inherits from a a base cache"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """A caching system"""

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return None
        # assigning the key:item value to paraent's instance variable
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves a key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
