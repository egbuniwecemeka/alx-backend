#!/usr/bin/env python3
"""FIFOCache class that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A basis FIFO caching system"""
    def __init__(self):
        """Initialize the parents class initializer"""
        super().__init__()

    def put(self, key, item):
        """Adds a key and its corresponding item to the cache"""
        if key is None or item is None:
            return
        
        self.cache_data[key] = item

        # FIFO Logic
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            fifo = self.cache_data.pop(first)
            print(f'DISCARD: {first}')
    
    def get(self, key):
        """Retrieves a key from the cache"""
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
    