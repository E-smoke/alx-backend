#!/usr/bin/env python3
"""Most Recently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    ama
    '''

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()


    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key)
            else:
                if key not in self.cache_data:
                    self.cache_data.popitem()
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key)
                else:
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key)


    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
