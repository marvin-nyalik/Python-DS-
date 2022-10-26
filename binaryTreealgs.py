class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self) -> str:
        return f'{self.val}'
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# DFS 
# push the root node if its not None
# pop the top node from the stack and print it
# push the right child then left child of the popped node on stack
# continue until the stack is empty
def dFS(node: Node):
    if node is None: return None
    stack = [node]
    print(stack)
    visited = []   
    while stack:
        v = stack.pop()
        visited.append(v.val)
        if v.right:
            stack.append(v.right)
        if v.left:
            stack.append(v.left)
            
    return visited   
print(dFS(a))   

#Recursive way
def dfsRec(node: Node):
    if node is None: return []
    lv = dfsRec(node.left)
    rv = dfsRec(node.right)
    return [node.val, *lv, *rv]

print(dfsRec(a))

#Breadth First Search
def bFS(root: Node):
    if root is None: return []
    queue = [root]
    while queue:
        v = queue.pop(0)
        print(v)
        if v.left:
            queue.append(v.left)
        if v.right:
            queue.append(v.right)
            
# bFS(a) 

# recursive BFS
def recBFS(root: Node):
    if root is None: return []
    print(root.val)
    recBFS(root.left)
    recBFS(root.right)
    
recBFS(a)
    
# Recursive tree includes: DFS Recursive
def treeIncludes(root: Node, target)-> bool:
    if root is None: return False
    if root.val == target: return True
    return treeIncludes(root.left, target) or treeIncludes(root.right, target)

print(treeIncludes(a, 'a'))

# iterative BFS soln
def itTreeIncludes(root: Node, target) -> bool:
    queue = [root]
    
    while queue:
        n = queue.pop(0)
        if n.val == target:
            return True
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return False  
print(itTreeIncludes(a, 'j'))
    
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
      
two.left = one
two.right = three
three.left = four
three.right = five

# tree sum ()
def treeSum(root: Node):
    if root is None: return 0
    return root.val + treeSum(root.left) + treeSum(root.right)
    
print(treeSum(two))

def treeMin(root: Node):
    if root is None: return float('inf')
    lv = treeMin(root.left)
    rv = treeMin(root.right)
    
    return min(root.val, lv, rv)
print(treeMin(two))

