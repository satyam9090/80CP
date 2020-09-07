class Node:
  def __init__(self, key):
    self.data = key
    self.next = None
  
class LinkedList:
  def __init__(self):
    self.head = None
  
  def Push(self, newNode):
    newNode.next = self.head
    self.head = newNode
  
  def Delete(self, node):
    branch = self.head
    if(branch.data == node.data):
      branch = branch.next
      branch.data = branch.next.data
      branch.next = branch.next.next
      return
    while(branch):
      if(branch.next.data == node.data):
        branch.next = branch.next.next
        break
      branch = branch.next
      if(branch.next is None):
        return

  def Print(self):
    branch = self.head
    while(branch):
      print(branch.data, end = '->')
      branch = branch.next
    print()

n = int(input("Enter number of Nodes: "))
LinkList = LinkedList()
for i in range(n):
  node = Node(int(input()))
  LinkList.Push(node)
  LinkList.Print()

n = int(input("Enter number of Elements to be Deleted: "))
for i in range(n):
  node = Node(int(input()))
  LinkList.Delete(node)
  LinkList.Print()
