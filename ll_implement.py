class Node:
  def __init__(self,prev,value,next):
    self.value = value
    self.next = next
    self.prev = prev

class Linked_list:
  def __init__(self,value):
    self.head = Node(None,value,None)
    self.tail = self.head
    self.length = 1

  def append(self,value):
      self.tail.next = Node(self.tail,value,None)
      self.tail = self.tail.next
      self.length+=1
  
  def prepend(self,value):
      self.head.prev = Node(None,value,self.head)
      self.head = self.head.prev
      self.length+=1

  def insert(self,index,value):
    if index == 0:
      self.prepend(value)
      return
    if index >= self.length:
      if index > self.length:
        print(f'Last node is at {self.length-1}')
        return
      self.append(value)
      return
    prev = self.traverse_to_index(index-1)
    prev.next = Node(prev,value,prev.next)
    self.length+=1

  def remove(self, index):
    if index >= self.length:
      raise IndexError('linked list index out of range')
    if index == 0:
      head = self.head
      self.head = head.next
      self.head.prev = None
      del head # not necessary 
      self.length-=1
      return
    if index == self.length-1:
      prev = self.traverse_to_index(self.length-1)
      del self.tail  # not necessary
      prev.next= None
      self.tail = prev
      self.length-=1
      return
    prev = self.traverse_to_index(index-1)
    crnt = prev.next
    prev.next = crnt.next
    crnt.next.prev = prev
    del crnt  # not necessary
    self.length-=1
    return


  def traverse_to_index(self,index):
    if index > self.length:
      raise IndexError('linked list index out of range')
    crnt = self.head
    for i in range(index):
      crnt = crnt.next
    return crnt

  def access(self):
      current = self.head
      while current is not None:
        print(current.value, end='')
        print(',', end='') if current.next is not None else None
        current = current.next
      print('\n')

  def reverse(self):
    first = self.head
    self.tail = self.head
    second = first.next
    while(second):
      temp = second.next
      second.next = first
      first=second
      second = temp
    self.head.next = None
    self.head = first
    return self.access()
print('\n')
ll = Linked_list(10)
ll.access()
ll.append(5)
ll.access()
ll.prepend(16)
ll.access()
ll.insert(1,"apple")
ll.access()
ll.insert(0,"android")
ll.access() 
ll.insert(4,"windows")
ll.access()
ll.reverse()
'''
####### ERRORS MADE ##############
  1. classes do not have () while creating them
  2. use object property with dot notation, 
    ['key'] is for dictionaries
##################################
'''