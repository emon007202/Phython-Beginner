# def test01 (a,b):
#     first = a+b
#     return first
#
#
# test01(7,9)
# test01(11,19)
# test01(15,16)
# print(test01(7,9))

def fizz_buzz (range_wanted):
    for i in range (1,range_wanted):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print (i)


#fizz_buzz(50)
#fizz_buzz(100)
