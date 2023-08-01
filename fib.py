from collections import defaultdict

# This is test so see the difference between time complexities.

# Brute force
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(4))
print(fib(5))
print(fib(35))

# Memoized

def mem_fib(n, memo = defaultdict()):
    
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = mem_fib(n - 1, memo) + mem_fib(n - 2, memo)
    return memo[n]


print(mem_fib(3))
print(mem_fib(4))
print(mem_fib(5))
print(mem_fib(35))