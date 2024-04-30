# 
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
my = MyIterator([1,2,3,4,5])
for item in my:
    print(item)

iter_obj = iter(my)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))