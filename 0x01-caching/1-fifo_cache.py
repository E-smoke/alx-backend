#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    '''
    ama
    '''
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                self.cache_data[key] = item
                print('DISCARD: {}'.format(first_key))
