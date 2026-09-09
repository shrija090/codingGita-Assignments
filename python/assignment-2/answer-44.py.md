price = "2500"
discount = "10"

price = float(price)
discount = float(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)