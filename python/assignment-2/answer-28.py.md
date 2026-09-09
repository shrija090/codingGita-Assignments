number = 234

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

product_of_digits = ones_digit * tens_digit * hundreds_digit

print("Product of Digits:", product_of_digits)