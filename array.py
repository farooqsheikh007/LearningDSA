class MyArray :
  def __init__(self):
    self.length = 0
    self.data = {}

  def get(self,index):
    return self.data.get(index)

  def push(self,item):
    self.data[self.length] = item
    self.length += 1
    return self.length

arr = MyArray();
print(arr.push("greater"))
print(arr)