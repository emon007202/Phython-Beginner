#Here’s a while loop that finds out the maximum power of n before the value exceeds 1000:
n = 2  # Could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print("Maximum power of", n," <1000 can be", power)

#The following loop computes the sum of the first and the last digits of any integer:
n = 249
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
    first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print("sum of 1st & last degit of", n, "is",result)

