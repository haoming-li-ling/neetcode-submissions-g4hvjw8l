class MyHashMap:

    def __init__(self):
        self.l = []
        

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.l):
            if k == key:
                self.l[i] = (key, value)
                return
        self.l.append((key, value))

        

    def get(self, key: int) -> int:
        for (k, v) in self.l:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for i, (k, _) in enumerate(self.l):
            if k == key:
                del self.l[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)