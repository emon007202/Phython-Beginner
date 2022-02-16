# Problem Statement#
# As we saw earlier, the Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. The first two numbers are 0 and 1:
#
# 0 1 1 2 3 5 8 13
# You must write the fib() function which takes in a positive integer, n, and returns the n-th Fibonacci number. However, instead of using recursion, your function must use any of the loops.
#
# Sample Input#
# n = 7
# Sample Output#
# 8
# Coding Challenge#
# Take some time to figure out how the recursive approach can be translated into an iterative one. Consider all edge cases that could occur.
#
# If n is negative or zero, return -1.

def fib(n):
    a = 0
    b = 1
    if n <0:
        return -1
    if n == 1:
        return a
    if n ==2:
        return b

    count = 3
    while count <= n:
        fib_nth = a+b
        a = b
        b = fib_nth
        count += 1
    return fib_nth

n = 7
print(fib(n))