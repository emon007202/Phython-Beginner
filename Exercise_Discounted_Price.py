# Problem Statement#
# In this challenge, you must discount a price according to its value.
#
# If the price is 300 or above, there will be a 30% discount.
#
# If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.
#
# If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.
#
# If the price is less than 100, there will be a 5% discount.
#
# If the price is negative, there will be no discount.
# Sample Input#
# price = 250
# Sample Output#
# price = 200

price = 250
if (price >= 300):
    dis_price = (price*30)/100
    price = price-dis_price
    print(price)
elif price >= 200 and price < 300:
    dis_price = (price*20)/100
    price= price-dis_price
    print(price)
elif price >= 100 and price <200:
    dis_price = (price * 10)/100
    price= price-dis_price
    print(price)
elif price <100:
    dis_price= (price* 5)/100
    price = price-dis_price
    print(price)


