#!/usr/bin/python3
"""LIFOCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system

        # # methods
        list(dict.keys())[-1]
        OrderedDict.popitem(last=True)
        next(reversed(dict))
    """
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds an item and removes the most recentitem if limit is exceeded"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.stack.remove(key)

        self.cache_data[key] = item  # Insert new key-item
        self.stack.append(key)  # Add key to insertion order

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.stack.pop(-2) # Remove second-last inserted key
            del self.cache_data[last]   # Delete from cache
            print(f'DISCARD: {last}')

    def get(self, key):
        """Retrieves a key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
