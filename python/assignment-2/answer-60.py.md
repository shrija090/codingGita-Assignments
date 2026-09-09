number = 5836

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + ones_digit

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

price = "1250"
quantity = "4"
discount = "10"

price = int(price)
quantity = int(quantity)
discount = int(discount)

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)


### Output
# text
# Thousands Digit: 5
# Hundreds Digit: 8
# Tens Digit: 3
# Ones Digit: 6
# Sum of Digits: 22
# Reversed Number: 6385
# Subtotal: 5000
# Discount Amount: 500.0
# Final Amount: 4500.0