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
    
    def put(self, key, item):
        """Adds an item and removes the most recentitem if limit is exceeded"""
        if key is None or item is None:
            return

        # If key already exists, update without discarding
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = next(reversed(self.cache_data))
            del self.cache_data[last]
            print(f'DISCARD: {last}')
        
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves a key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
