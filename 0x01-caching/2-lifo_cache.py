#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                tup = self.cache_data.popitem()
                self.cache_data[key] = item
                print('DISCARD: {}'.format(tup[0]))


    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
        return None
