price = "2000"
discount = "15"

price = int(price)
discount = int(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)