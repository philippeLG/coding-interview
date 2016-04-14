# Hastable implementation

class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value

    def __str__(self):
        return str(self.value)

class HashTable:
    table_size=20
    def __init__(self):
        self.list=[None]*self.table_size

    def hash_function(self,key_str, size):
        return sum([ord(c) for c in key_str]) % size

    def get(self,key):
        index = self.hash_function(key,self.table_size)
        return self.list[index]

    def set(self,key,value):
        key_value = KeyValue(key,value)
        index = self.hash_function(key,self.table_size)
        self.list.insert(index,key_value)

hashTable= HashTable()
hashTable.set("hello","hola")
print hashTable.get("hello")
