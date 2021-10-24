class MyArray:
    def __init__(self):
      self.length = 0
      self.data = {}

    def get(self, index):
      return self.data.get(index)

    def push(self, item):
      self.data[self.length] = item
      self.length += 1
      return self.length

    def pop(self):
      last_item = self.data[self.length-1]
      del self.data[self.length-1]
      self.length -= 1
      return last_item

    def delete(self,index):
      item = self.data[index]
      self.shift_items(index)
      self.pop()
      return item

    def shift_items(self,index):
      for i in range(index, self.length-1):
        self.data[i] = self.data[i+1]

    def __str__(self):
      return f"length: {self.length}, data: {self.data}"


arr = MyArray()
arr.push("one")
arr.push("two")
arr.push("three")
print(arr.delete(0))
print(arr)
