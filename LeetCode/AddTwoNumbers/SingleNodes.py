class SingleNodes :
     def __init__(self,data):
      self.data = data
      self.next = None

 # traversing a Linked list
 # this gives me a idea , how about we build a number while traversiong 
 # Shouldd i put it in a list ? or a string ? 
#lets try List
# node1 = SingleNodes(15)
# node2 = SingleNodes(30)
# node3 = SingleNodes(50)





 
node11 = SingleNodes(1)
node12 = SingleNodes(2)
node13 = SingleNodes(3)

node21 = SingleNodes(4)
node22 = SingleNodes(5)
node23 = SingleNodes(6)

node11.next = node12
node12.next = node13
node21.next = node22
node22.next = node23





head = node11 
head2 = node21
current = head 
current2 = head2
list1 = []
list2 =[]
while current is not None:
    list1.append(current.data)
    print(current.data)
    current = current.next
    
while current2 is not None:
   list2.append(current2.data)
   print(current2.data) 
   current2 = current2.next

la = list1[::-1]
lb = list2[::-1]
print(la)

print(lb)
finallist = ''.join (map(str, la))
finallist2 = ''.join (map(str, lb))
print(finallist)
print(finallist2)
FinalList = int(finallist) + int(finallist2)
print(FinalList)
ListToNodes = list(str(FinalList))
head1 = None
current3 = None
for value in ListToNodes:
   newnode = SingleNodes(value)
   if head1 is None:
    head1 = current3 = newnode
   else:
    current3.next = newnode
    current3 = newnode
 
   


# head = node1
# current = head 
# while current: 
#    print(current.data , end="-->")
#    current = current.next
#    print("none")


#seems like trying to cheat with normal lists wont work 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#  def __init__(self,data):
#     self.data = data
#     self.next = None
  
 
# l1 = [7,2,5]
# la = l1[::-1]
# l2 = [2,3,6]
# lb = l2[::-1]


  
# FinalList1= ''.join(map(str , la))
# FinalList2= ''.join(map(str , lb))
# last = int(FinalList2)+int(FinalList1)
# gigi = map(int,list(str(last)))

# print(list(gigi))