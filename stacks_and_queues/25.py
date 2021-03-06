# LRU Cache Implementationa

from collections import OrderedDict
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.cache = OrderedDict()
        self.cap = cap
        
    #Function to return value corresponding to the key.
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            # move the recently accessed key to the end
            self.cache.move_to_end(key)
            return self.cache[key]

    #Function for storing key-value pair.  
    def set(self, key, value):
        # add the value of the key or update the value
        self.cache[key] = value
        self.cache.move_to_end(key)

        # if capcity is exceeded
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)