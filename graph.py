# Graph rep: Collection of nodes + Dict<<Adjacency list>>
from itertools import count


graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
 }

#Graph Iterative DFS
def depthFirstSearch(graph, a) -> str:
    stack = [a]
    while stack:
        y = stack.pop()
        print(y)
        for i in graph[y]:
            stack.append(i)
    return f'Traversal done'
    
# depthFirstSearch(graph, 'a')

#Graph Recursive DFS
def recDepthFirstSearch(graph, a):
    print(a)
    y = graph[a]
    for i in y:
        recDepthFirstSearch(graph, i)
# recDepthFirstSearch(graph, 'a')

def breadthFirstSearch(graph, a):
    queue = [a]
    while(queue):
        y = queue.pop(0)
        print(y)
        for i in graph[y]:
            queue.append(i)
            
breadthFirstSearch(graph, 'a')
            
# Does a path exist between the given source and destination nodes?
def hasPath(graph, source, dest)-> str:
    stack = [source]
    while(stack):
        path = stack.pop()
        for neighbor in graph[path]:
            stack.append(neighbor)
            if neighbor is dest:
                return f'There exists a path between {source} and {dest}'
    return f'Theres no path between {source} and {dest}'

print(hasPath(graph, 'b', 'e'))

#Recursive has Path
def recHasPath(graph, src, dest)->bool:
    if src is dest: return True
    for i in graph[src]:
        recHasPath(graph, i, dest)
    return False

print(recHasPath(graph, 'b', 'e'))

# Dealing with cyclic graphs
# Soln: Mark the visited nodes as visited to avoid exploring them again
# The Undirected Graph issue : A path goes both ways

# given a collection of edges make a graph adjacencty list
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def makeGraphAdjList(edges):
    graph_list = {}
    for e in edges:
        a, b = e
        if a not in graph_list: graph_list[a] = []
        if b not in graph_list: graph_list[b] = []
        
        graph_list[a].append(b)
        graph_list[b].append(a)
        
    return graph_list        
print(makeGraphAdjList(edges))


# def hasPathRecursive(graph, src, dest, visited = [])->bool:
#     if src is dest: return True
#     if src in visited: return False

#     visited.append(src)
#     for i in graph[src]:
#         hasPathRecursive(graph, i, dest, visited)
#     return False
    
# print (hasPathRecursive(makeGraphAdjList(edges), 'i','k', []))

def undirectedPath(edges, node, node2):
    graph = makeGraphAdjList(edges)
    tr_set = set()
    return hasPathRec(graph, node, node2, tr_set)

def hasPathRec(graph, src, dest, st):
    if src is dest: return True
    if src in st: return False
    
    st.add(src)
    for i in graph[src]:
        if hasPathRec(graph, i, dest, st): return True
    return False
    
print(undirectedPath(edges, 'i', 'm'))
    
# Connected components problem
def connCompCount(graph):
    count = 0
    visited = set()
    for i in graph:
        if explore(graph, i, visited): count+= 1
    return count

def explore(graph, node, visited):
    # do a recursive dfs for every node in graph
    # Doesnt have to be recursive could as well be iterative
    if node in visited: return False
    visited.add(node)
    for neighbor in graph[node]:
        explore(graph, neighbor, visited)
    return True
print(connCompCount(makeGraphAdjList(edges))) #should return 2 and does


# connected components
def countConnComp(graph):
    count = 0
    visited = set()
    for i in graph:
        if explGraph(graph, i, visited):
            count += 1
    return count

def explGraph(graph, node, visited):
    if node in visited: return False
    visited.add(node)
    
    for neighbor in graph[node]:
        explGraph(graph, neighbor, visited)
    return True

print(countConnComp(makeGraphAdjList(edges)))

def largestComponent(graph):
    largest = 0
    visited = set()
    for i in graph:
        size = searchLargestComp(graph, i, visited)
        if size > largest:
            largest = size
    return largest

def searchLargestComp(graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    count = 1
    for neighbor in graph[node]:
        count += searchLargestComp(graph, neighbor, visited)
    return count

print(largestComponent(makeGraphAdjList(edges)))

print(largestComponent({
    '0':['8','1','5'],
    '1':['0'],
    '5':['0','8'],
    '8':['0', '5'],
    '2':['3','4'],
    '3':['2','4'],
    '4':['3', '2']
}))