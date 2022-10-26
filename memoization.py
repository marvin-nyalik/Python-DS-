# given a fibonaci sequence, it takes O(2*n)
# with memoization, the algorithm can be improved to o(n)
# at the cost of using extra memory

def fibonacci(n, memo= {}):
    if n <= 2: return 1
    if n in memo: return memo[n]
    
    item = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = item
    return item

print(fibonacci(50)) #fib(50) now computes really fast thanks to memoization


# Another case using memoization technique
# Given a grid, in how many ways can you move
# from top left to bottom right
# if you can only move right or bottom
# We are using memoization to enhance the
# efficiency of the algorithm for larger numbers
def gridTraveller(m, n, mem = {}):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    cord = str(m) + ',' + str(n)
    if cord in mem: return mem[cord]
    
    
    res = gridTraveller(m-1, n) + gridTraveller(m, n-1)
    mem[cord] = res
    return res
print(gridTraveller(18,18))
