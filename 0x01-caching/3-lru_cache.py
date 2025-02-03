#!/usr/bin/python3
"""LRUCache class inheriting from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Initialize the class"""
    def __init__(self):
        """Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache using LRU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # if key exists, key will be removed from the stack (re-added later)
            self.stack.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used key. (First item in list)
            lru_key = self.stack.pop(0)
            del self.cache_data[lru_key]
            print(f'DISCARD: {lru_key}')

        # Add key to cache as the recently used key
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Get an item from the cache using its key"""
        if key is None or key not in self.cache_data:
            return None
        
        # Move key to end of list (Marked as recently used)
        self.stack.remove(key)
        self.stack.append(key)

        return self.cache_data[key]
