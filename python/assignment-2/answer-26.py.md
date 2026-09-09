number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

sum_of_digits = ones_digit + tens_digit + hundreds_digit

print("Sum of Digits:", sum_of_digits)