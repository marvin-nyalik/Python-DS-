# Graph rep: Collection of nodes + Dict<<Adjacency list>>
from itertools import count

# b - a - c - e

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

# finding the shortest path to a node
def shortestDist(graph, src, dest):
    queue = [(src,0)]
    visited = set()
    visited.add(src)
    while queue:
        y = queue.pop(0)
        node, dist = y
        if node is dest:
            return dist
        for n in graph[node]:
            if n not in visited: visited.add(n)
            queue.append((n, dist + 1))
    return -1

print(shortestDist(graph, 'b', 'e'))

# The island count
g = [
    ['0', '1', '0','0','1'],
    ['1', '0', '0','1','1'],
    ['1', '0', '1','1','1']
]

# def islandCount(grid):
#     count = 0
#     visit = set()
#     for r in range(len(grid)):
#         for c in range(len(grid[r])):
#             if explore(grid, r, c, visit): count += 1
            
#     return count  

# def explore(grid, r, c, visit):
#     rowInbounds = 0 <= r and r <= len(grid)
#     colInbounds = 0 <= c and c <= len(grid[r])
    
#     if not (rowInbounds and colInbounds): return False
#     if grid[r][c] is 'W': return False
#     pos = str(r) + ',' + str(c)

#     if pos in visit: return False
#     visit.add(pos)
    
#     explore(grid, r-1, c, visit)
#     explore(grid, r+1, c, visit)
#     explore(grid, r, c-1, visit)
#     explore(grid, r, c+1, visit)
    
#     return True

    
def numIslands(grid) -> int:
    count = 0
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if explore(grid, row, col, visited): count += 1
    return count
    
def explore(grid, row, col, visited):
    rowInbound = 0 <= row and row <= len(grid)
    colInbound = 0 <= col and col <= len(grid[0])
    bound = rowInbound and colInbound
    if not bound: return False
    if grid[row][col] is "0": return False
    position = str(row) + ',' + str(col)
    if position in visited: return False
    
    visited.add(position)
    
    explore(grid, row+1, col, visited)
    explore(grid, row-1, col, visited)
    explore(grid, row, col+1, visited)
    explore(grid, row, col-1, visited)
    
    return True

g2 = [
  ["1","1","1","0","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    ]
print(numIslands(g2))

def minIsland(grid):
    min_island = float('inf')
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if findMinIsland(grid, row, col, visited) < min_island and findMinIsland(grid, row, col, visited) > 0:
                    min_island = findMinIsland(grid, row, col, visited)
    return min_island

def findMinIsland(g, r, c, visited):
    rowInbound = 0 <= r and r <= len(g)
    colInbound = 0 <= c and c <= len(g[r])
    
    size = 1
    if not (rowInbound and colInbound): return 0
    if g[r][c] is '0': return 0
    
    pos = str(r) + "," + str(c)
    if pos in visited: return 0
    visited.add(pos)
    
    size += findMinIsland(g, r+1, c, visited)
    size += findMinIsland(g, r-1, c, visited)
    size += findMinIsland(g, r, c+1, visited)
    size += findMinIsland(g, r, c-1, visited)
    
    return size
print(minIsland(g2))