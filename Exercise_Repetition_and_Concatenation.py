# Problem Statement#
# In this exercise, you must implement the rep_cat function. You are given two integers, x and y, as arguments. You must convert them into strings. The string value of x must be repeated 10 times and the string value of y must be repeated 5 times.
#
# At the end, y will be concatenated to x and the resulting string must returned.
#
# Sample Input#
# x = 3
# y = 4
# Sample Output#
# '333333333344444'

def rep_cat(x,y):
    z = (str(x)*10+str(y)*5)
    return z

a = 3
b = 4

print(rep_cat(x=a,y=b))
