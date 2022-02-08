# Problem Statement#
# In this challenge, you must implement the factorial() function. It takes an integer as a parameter and calculates its factorial. Python does have a built-in factorial function but you’ll be creating your own for practice.
#
# The factorial of a number, n, is its product with all the integers between 0 and n.
#
# svg viewer
# The factorial for 0 and 1 is always 1.
#The input will always be an integer, so you don’t need to worry about that. If the integer is negative, the function always returns -1.
# Sample Input#
# n = 5
# Sample Output#
# 120

def factorial(n):
    if (n ==1 or n==0):
        return 1
    elif (n<0):
        return -1
    else:
        return n*factorial(n-1)



n = 5
print(factorial(n))