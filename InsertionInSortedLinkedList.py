class Node:
  def __init__(self, key):
    self.data = key
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def SortedInsert(self, newNode):
    if self.head is None:
      self.head = newNode
    elif(self.head.data > newNode.data):
      newNode.next = self.head
      self.head = newNode
    else:
      tree = self.head
      while((tree.next is not None) and (tree.next.data < newNode.data)):
        tree = tree.next
      newNode.next = tree.next
      tree.next = newNode
  
  def PrintLinkedList(self):
    node = self.head
    while(node):
      print(node.data, end = "->")
      node = node.next

n = int(input())
linkList = LinkedList()
for i in range(n):
  x = Node(int(input()))
  linkList.SortedInsert(x)

linkList.PrintLinkedList()

