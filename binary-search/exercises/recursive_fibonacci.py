"""
Recursive fibonacci
Having into account that fn = fn-1 + fn -2
"""

def r_fib(n):
    if n < 2:
        return n
    return r_fib(n-1) + r_fib(n-2)

for x in range(10):
    print(r_fib(x))
