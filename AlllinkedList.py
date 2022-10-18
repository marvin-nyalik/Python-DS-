class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self) -> str:
        return f'Node with value {self.val}'
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

#iterative method
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(f'{curr.val}')
        curr = curr.next

printLinkedList(a)

# General rule of recursion
# step 1: Define a terminating condition
# step 2: Define the logic in the recursive fxn
# step 3: Let the fxn call itself passing in the updated parameters
# Recursive method
def recLinkedList(head):
    if head is None: return None #recursive terminating condition
    print(f'{head.val}')         #recursive fxn logic
    recLinkedList(head.next)     #recursive call with updated parameter
    
recLinkedList(a)

#recursive version
def linkedListVals(head, vals = []):
    if head is None: return          #recursive terminating condition
    vals.append(head.val)            #recursive fxn logic
    linkedListVals(head.next, vals)  #recursive call with updated parameters
    return vals

print(linkedListVals(a))

#Iterative version
def itLinkedListVals(head):
    val = []
    curr = head 
    while curr is not None:
        val.append(curr.val)
        curr = curr.next
    return val

print(itLinkedListVals(a))

#sum list problem: Iterative version
def linkedListSum(head):
    curr = head
    totalSum = 0
    while curr is not None:
        totalSum += curr.val
        curr = curr.next
    print(totalSum)

#Recursive version
def sumIter(head):
    if head is None: return 0             #recursive terminating condition
    return head.val + sumIter(head.next)  #recursive logic + recursive call with updated parameter

#find element in linked list
def findEl(head, target):
    if head is None: return False
    if head.val == target: return True
    return findEl(head.next, target) 

#get node value
def nodeValue(head, index):
    if head is None: return None
    if index == 0: return head.val
    nodeValue(head.next, index - 1)
    
#get node value iterative version
def getNodeValue(head, index):
    curr = head 
    if head is None: return None
    if index == 0: return head.val
    while(index > 0):
        curr = curr.next
        index -= 1
        if index == 0 and curr is not None:
            return curr.val
        return None

#reverse a linked list
def revLinkedList(head):
    curr = head
    prev = None
    while(curr is not None):
        next = curr.next
        curr.next = prev 
        prev = curr
        curr = next
    return f'{prev}'

#recursive reverse
def recRev(head, prev=None):
    if head is None: return prev
    next = head.next
    head.next = prev
    return recRev(next, head)

one = Node(1)
two = Node(2)
three = Node(3)

one.next = two
two.next = three
# print(sumIter(one))  
# print(linkedListSum(one)) 
print(findEl(one, 4))
# print(getNodeValue(one, 1)) 
# revLinkedList(one)
# print(recRev(one, None))

def zipperList(head: Node, head2:Node)-> Node:
    count = 0
    curr1 = head.next
    curr2 = head2
    tail = head
     
    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        elif count % 2 != 0:
            tail.next = curr1
            curr1 = curr1.next
        count += 1
        tail = tail.next
        
    if curr1 is None:
        tail.next = curr2
    if curr2 is None:
        tail.next = curr1 
    # 1 -> 2 -> 3
    # a -> b -> c
    # 1 -> a -> 2-> b -> 3 -> c
    return head
printLinkedList(zipperList(a, one))

