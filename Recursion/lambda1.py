#suppose a product costs Rs.1000 and has a 10% percent discount write a program 
#to calculate discounted price using lambda function


calculate_discount = lambda price, discount: price - (price * discount / 100)
cost = 100
discount_percent = 10
final_price = calculate_discount(cost, discount_percent)
print("Discounted Price:", final_price)

