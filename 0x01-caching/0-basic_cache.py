#!/usr/bin/env python3
"""Basic caching module.
"""

from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
        return None
