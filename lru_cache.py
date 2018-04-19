from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = OrderedDict()
        self.current_capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print('During get of',key,':',self.dict)
        if key not in self.dict:
            return -1
        value = self.dict[key]
        del self.dict[key]
        self.dict[key] = value
        return value



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print('during put of ',key,value)

        if key in self.dict:
            del self.dict[key]
        else:
            if self.current_capacity > 0:
                self.current_capacity -= 1
            else:
                self.dict.popitem(last = False)
        self.dict[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
